// enum
enum Status {
  PENDING, // 0
  IN_PROGRESS, // 1
  DONE, // 2
  CANCELLED, // 3
  }
enum Status1 {
  PENDING = 3, // 3
  IN_PROGRESS, // 4
  DONE, // 5
  CANCELLED, // 6
  }
enum Status2 {
  PENDING = 3,
  IN_PROGRESS = 5,
  DONE = 8,
  CANCELLED = 10,
  }

const stats1: Status = Status.PENDING;
const stats2: Status = 1;