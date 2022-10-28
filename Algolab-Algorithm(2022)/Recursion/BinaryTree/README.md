# 이진검색트리(Recursion)

다음과 같은 노드 구조를 가진 이진검색트리의 관련함수를 모두 재귀함수로 구현하는 프로그램 을 작성하시오.

struct node
{
int data; // 노드에 저장되는 정수 데이터
struct node* left; // 왼쪽 서브트리
struct node* right; // 오른쪽 서브트리
}

(1) void insert(struct node\*\* root, int data);
루트노드가 root 인 이진검색트리에 데이터 data 를 입력하는 함수. 각 노드는 동적으로 메모리를 할당하여 구현한다.

(2) void preOrder(struct node\* root);
루트노드가 root 인 이진검색트리를 전위(preorder) 탐색하면서 모든 노드에 저장된 데이터 를 한 줄에 출력.

(3) void inOrder(struct node\* root);
루트노드가 root 인 이진검색트리를 중위(inorder) 탐색하면서 모든 노드에 저장된 데이터를 한 줄에 출력.

(4) void postOrder(struct node\* root);
루트노드가 root 인 이진검색트리를 후위(postorder) 탐색하면서 모든 노드에 저장된 데이터 를 한 줄에 출력.

(5) int size(struct node\* root);
루트노드가 root 인 이진검색트리의 모든 노드의 개수를 계산함.

(6) int height(struct node\* root);
루트노드가 root 인 이진검색트리의 높이를 계산함.

(7) int sumOfWeight(struct node\* root);
루트노드가 root 인 이진검색트리의 모든 노드에 저장된 데이터의 합을 계산함.

(8) int maxPathWeight(struct node\* root);
루트노드가 root 인 이진검색트리의 루트노드부터 단말노드까지의 경로 상의 모든 노드에 저 장된 데이터의 합이 가장 큰 합을 계산함.

(8) void mirror(struct node\*\* root);
루트노드가 root 인 이진검색트리를 미러 이지미가 되도록 노드의 순서를 변환함.

(9) void destruct(struct node\*\* root);
루트노드가 root 인 이진검색트리의 동적으로 메모리 할당된 노드를 해제하여 이진검색트리 를 소멸시킴.

## 입력

입력은 표준입력(standard input)을 사용한다. 입력은 𝑡개의 테스트 케이스로 주어진다. 입력의 첫 번째 줄에 테스트 케이스의 개수를 나타내는 정수 𝑡가 주어진다. 두 번째 줄부터 t 개의 줄에 는 한 줄에 한 개의 테스트 케이스에 해당하는 데이터가 입력된다. 각 줄에서 첫 번째로 입력되 는 정수 𝑛(1≤𝑛≤100)은 이진검색트리에 입력되는 정수 데이터의 개수를 나타낸다. 그 다음으 로는 𝑛𝑛개의 정수가 입력된다. 이 정수들은 최소 1이며 최대 10,000이며, 또한 이 정수들은 모 두 다른 수이다. 각 정수들 사이에는 한 개의 공백이 있으며, 잘못된 데이터가 입력되는 경우는 없다.

## 출력

출력은 표준출력(standard output)을 사용한다. 입력되는 테스트 케이스의 순서대로 다음 줄에 이어서 각 테스트 케이스의 결과를 출력한다. 각 테스트 케이스의 출력되는 첫 줄에 입력으로 주 어진 데이터에 대하여 이진검색트리의 함수들이 실행된 결과를 출력한다.

## 입력과 출력의 예

|                      입력                       |                                                                                                   출력                                                                                                    |
| :---------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| 3 <br/> 5 3 4 5 1 2 <br/> 1 1 <br/> 5 1 2 3 4 5 | 5 <br/> 2<br/>15<br/>12<br/> 3 4 5 1 2<br/> 5 4 3 2 1<br/> 5 4 2 1 3<br/> 0<br/>1<br/>0<br/>1<br/>1<br/>1<br/>1<br/>1<br/>0<br/>5<br/>4<br/>15<br/>15<br/> 1 2 3 4 5<br/> 5 4 3 2 1<br/> 5 4 3 2 1<br/> 0 |