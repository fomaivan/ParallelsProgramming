#include <mpi.h>
#include <unistd.h>
#include <fstream>
#include <iomanip>
#include <iostream>

double Func( double x ) {
  return 4 / ( 1 + x * x );
}

double NumericIntegral(double a, double b, int n) {
  const double width = (b - a) / n;

  double res = 0.0;
  for (int step = 0; step < n; ++step) {
    const double x1 = a + step * width;
    const double x2 = a + (step + 1) * width;
    res += 0.5 * (x2 - x1) * (Func(x1) + Func(x2));
  }
  return res;
}

int main(int argc,char* argv[]) {
  std::ofstream out;
  out.open("data.txt", std::ios::app);

  double res_arr[10]; 
  int n, size_process, i, j, id_process, source, dest, tag;
  double my_a, my_b, my_range = 0.0;
  double h, result, a, b, num;
  double curr_time, start_time, end_time, tmp_res_integral;

  MPI_Status status;
  n = atoi(argv[1]);

  a = 0.0, b = 1.0;
  dest = 0, tag = 77;
  result = 0.0;

  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &id_process);
  MPI_Comm_size(MPI_COMM_WORLD, &size_process);

  start_time = MPI_Wtime();

  my_range = (b - a) / size_process;
  my_a = a + id_process * my_range;
  my_b = my_a + my_range;
  num = n / size_process;

  tmp_res_integral = NumericIntegral(my_a, my_b, num);
  printf("Process %d has the partial result of %lf\n", id_process, tmp_res_integral);
  if (id_process == 0) {
    result += tmp_res_integral;
    for (i = 1; i < size_process; i++) {
      MPI_Recv(&tmp_res_integral, 1, MPI_DOUBLE, i, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      result += tmp_res_integral;
    }
    std::cout << "Sum of part = " << result << std::endl;
    std::cout << "Single process result = " << NumericIntegral(0.0, 1.0, n) << std::endl;
    out << "N=" << n << ", " << "p=" << size_process << ", time=" << MPI_Wtime() - start_time << std::endl;
  } else {
    MPI_Send(&tmp_res_integral, 1, MPI_DOUBLE, dest, tag, MPI_COMM_WORLD);
  }
  MPI_Finalize();
  out.close();
  return 0;
}

