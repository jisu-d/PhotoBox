
<style>
    td{
        text-align: center;
    }
</style>


## 프로젝트 소개
본 프로젝트는 기존 포토부스의 이동의 불편함을 개선하기 위해 기획 및 제작 하였습니다.


## 기능

<table>
  <thead>
    <tr>
      <th style="width: calc(100% / 3);">start_page</th>
      <th style="width: calc(100% / 3);">select_design</th>
      <th style="width: calc(100% / 3);">capture_imgs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class=""><img src="/readme_img//start_page.png" width="300px"></td>
      <td><img src="/readme_img///select_design.png" width="300px"></td>
      <td><img src="/readme_img//capture_imgs.gif" width="300px"></td>
    </tr>
    <tr>
      <td>처음 시작 페이지 이므로 화면 중간에 있는 버튼을 클릭하면 사진촬영이 시작됨.</td>
      <td>프레임 디자인을 선택하는 페이지 이미지임. 좌우로 움직여 다른 디자인 선택이 가능함</td>
      <td>총 6장의 사진을 3초 간격으로 촬영하며, 2초의 대기 시간이 있다.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th style="width: calc(100% / 3);">select_imgs</th>
      <th style="width: calc(100% / 3);">check_made_img</th>
      <th style="width: calc(100% / 3);">print_wait</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="/readme_img//select_imgs.png" width="300px"></td>
      <td><img src="/readme_img///check_made_img.png" width="300px"></td>
      <td><img src="/readme_img//print_wait.png" width="300px"></td>
    </tr>
    <tr>
      <td>촬영한 6장의 사진 중 프레임에 합성할 4장의 사진을 선택하는 페이지임.</td>
      <td>합성된 이미지를 확인하고 몇장을 인쇄할 것 인지 선택하고 버튼을 클릭하는 페이지임.</td>
      <td>이미지가 인쇄하는 동안 대기하는 페이지임.</td>
    </tr>
  </tbody>
</table>


## 기술

### Frontend
- svelteKit
- tailwindcss
- flowbite

### Backend
- FastAPI
- OpenCV

## 하드웨어 제작

### 외관 경관
<table>
  <tbody>
    <tr>
      <td><img src="/readme_img//obj_img.png" width="300px"></td>
    </tr>
    <tr>
      <td>Fusion 360을 사용해 설계함.</td>
    </tr>
  </tbody>
</table>

### 물품 구매 목록
<table>
  <thead>
    <tr>
      <th style="width: 10%;">넘버</th>
      <th style="width: 35%">상품명</th>
      <th style="width: 10%">수량</th>
      <th style="width: 40%">용도</th>
      <th style="width: 5%">구매경로</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Witrue HD 4K 렌즈 CS 마운트 12MP 5MM</td>
      <td>1</td>
      <td>이미지 센서 광각렌즈</td>
      <td><a href="https://ko.aliexpress.com/item/1005004817099124.html?spm=a2g0o.order_list.order_list_main.5.44ec140fqnkfDq&gatewayAdapt=glo2kor" >링크</a></td>
    </tr>
    <tr>
      <td>2</td>
      <td>ZEUSLAP Z10T</td>
      <td>1</td>
      <td>UI UX 조작을 위한 터치 디스플레이</td>
      <td><a href="https://ko.aliexpress.com/item/1005005927975071.html?spm=a2g0o.order_list.order_list_main.10.44ec140fqnkfDq&gatewayAdapt=glo2kor" >링크</a></td>
    </tr>
    <tr>
      <td>3</td>
      <td>라즈베리파이5 8GB (Raspberry Pi 5)</td>
      <td>1</td>
      <td>메인 컴퓨팅 작업을 할 보드</td>
      <td><a href="https://www.eleparts.co.kr/goods/view?no=13323153#goodContent_7" >링크</a></td>
    </tr>
    <tr>
      <td>4</td>
      <td>라즈베리파이 액티브 쿨러 (Raspberry Pi Active Cooler)</td>
      <td>1</td>
      <td>라즈베리파이 쿨러</td>
      <td><a href="https://www.eleparts.co.kr/goods/view?no=13535082" >링크</a></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Raspberry Pi High Quality Camera</td>
      <td>1</td>
      <td>라즈베리파이와 직접적으로 연결하여 사진을 촬영할 이미지센서</td>
      <td><a href="https://www.eleparts.co.kr/goods/view?no=9471110" >링크</a></td>
    </tr>
    <tr>
      <td>6</td>
      <td>16mm C-mount lens</td>
      <td>1</td>
      <td>이미지 센서 망원렌즈</td>
      <td><a href="https://www.eleparts.co.kr/goods/view?no=9546893#goodContent_1" >링크</a></td>
    </tr>
    <tr>
      <td>7</td>
      <td>라즈베리파이 카메라 케이블 300mm</td>
      <td>1</td>
      <td>카메라와 라즈베리파이를 연결하는 케이블</td>
      <td><a href="https://www.eleparts.co.kr/goods/view?no=13535083#goodContent_2" >링크</a></td>
    </tr>
    <tr>
      <td>8</td>
      <td>ULTRA (스마트폰&태블릿전용) MicroSDXC 64GB [SDSQUNR-064G-GN3MN]</td>
      <td>1</td>
      <td>라즈베리파이 운영체제가 저장될 SD카드</td>
      <td><a href="https://www.eleparts.co.kr/goods/view?no=9736911" >링크</a></td>
    </tr>
    <tr>
      <td>9</td>
      <td>1/4 20pcs 삽입너트</td>
      <td>1</td>
      <td>완성된 본체와 삼각대 볼트에 연결하기 위한 부속품</td>
      <td><a href="https://ko.aliexpress.com/item/1005005220715165.html?spm=a2g0o.order_list.order_list_main.5.1d94140fACVFI2&gatewayAdapt=glo2kor" >링크</a></td>
    </tr>
    <tr>
      <td>10</td>
      <td>94x50mm 12V 20W RA 90 CRI LED 조명 패널</td>
      <td>2</td>
      <td>조명 역할을 해줄 LED패널</td>
      <td><a href="https://ko.aliexpress.com/item/1005002074669678.html?spm=a2g0o.order_detail.order_detail_item.4.6ae05ccdnX7X1e&gatewayAdapt=glo2kor" >링크</a></td>
    </tr>
    <tr>
      <td>11</td>
      <td>호후 스팀덱 스마트폰 C TO C 90도 직각 미니 젠더 2p</td>
      <td>1</td>
      <td>터치스크린 C타입 단자에 사용하기 위함.</td>
      <td><a href="https://smartstore.naver.com/amnet/products/8757468455?NaPm=ct%3Dlz70x64p%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D7aaee4897a0276444902bfbcce34fe559259bffc" >링크</a></td>
    </tr>
    <tr>
      <td>12</td>
      <td>USB 미니 5핀 케이블 1M C0573</td>
      <td>1</td>
      <td>이미지 프린터와 라즈베리파이를 연결하기 위함.</td>
      <td><a href="https://smartstore.naver.com/amnet/products/8757468455?NaPm=ct%3Dlz70x64p%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D7aaee4897a0276444902bfbcce34fe559259bffc" >링크</a></td>
    </tr>
    <tr>
      <td>13</td>
      <td>3mm 반투명 검정(스모그) [153(mm) x 440(mm)]</td>
      <td>2</td>
      <td>외관 아크릴 부속품</td>
      <td><a href="https://www.akobigs.com/shop/goods/goods_view.php?inflow=naverCheckout&goodsno=27912&NaPm=ct%3Dlz71bze9%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D3319a83fb897ac9e5f6eb1270a6aa9d94302d42a" >링크</a></td>
    </tr>
    <tr>
      <td>14</td>
      <td>3mm 반투명 검정(스모그)[230(mm) x 153(mm)]</td>
      <td>2</td>
      <td>외관 아크릴 부속품</td>
      <td><a href="https://www.akobigs.com/shop/goods/goods_view.php?inflow=naverCheckout&goodsno=27912&NaPm=ct%3Dlz71bze9%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D3319a83fb897ac9e5f6eb1270a6aa9d94302d42a" >링크</a></td>
    </tr>
    <tr>
      <td>15</td>
      <td>3mm 반투명 검정(스모그) [171(mm) x 50(mm)]</td>
      <td>2</td>
      <td>외관 아크릴 부속품</td>
      <td><a href="https://www.akobigs.com/shop/goods/goods_view.php?inflow=naverCheckout&goodsno=27912&NaPm=ct%3Dlz71bze9%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D3319a83fb897ac9e5f6eb1270a6aa9d94302d42a" >링크</a></td>
    </tr>
    <tr>
      <td>16</td>
      <td>2mm 반투명 백색  [79(mm) x 50(mm)]</td>
      <td>2</td>
      <td>외관 아크릴 부속품</td>
      <td><a href="https://www.akobigs.com/shop/goods/goods_view.php?inflow=naverCheckout&goodsno=27912&NaPm=ct%3Dlz71bze9%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D3319a83fb897ac9e5f6eb1270a6aa9d94302d42a" >링크</a></td>
    </tr>
    <tr>
      <td>17</td>
      <td>3mm 반투명 검정(스모그) [230(mm) x 440(mm)]</td>
      <td>1</td>
      <td>외관 아크릴 부속품</td>
      <td><a href="https://www.akobigs.com/shop/goods/goods_view.php?inflow=naverCheckout&goodsno=27912&NaPm=ct%3Dlz71bze9%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D3319a83fb897ac9e5f6eb1270a6aa9d94302d42a" >링크</a></td>
    </tr>
    <tr>
      <td>18</td>
      <td>3mm 반투명 검정(스모그) [230(mm) x 440(mm)](도면전달)</td>
      <td>1</td>
      <td>외관 아크릴 부속품</td>
      <td><a href="https://www.akobigs.com/shop/goods/goods_view.php?inflow=naverCheckout&goodsno=25555&NaPm=ct%3Dlz71bj6f%7Cci%3Dcheckout%7Ctr%3Dppc%7Ctrx%3Dnull%7Chk%3D2745a5cd976a8510fc84692e902cd65f79c7b6e8" >링크</a></td>
    </tr>
</table>