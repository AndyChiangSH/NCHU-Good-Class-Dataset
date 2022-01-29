# NCHU-Good-Class-Dataset

> 中興好課 - 課程資料前處理

## 說明

此為[中興好課(NCHU Good Class)](https://github.com/AndyChiangSH/NCHU-Good-Class)課程資料前處理程式，請後續維護人員**每學期**更新一次課程資料。

## 使用

### 1. Clone repository

```
git clone https://github.com/AndyChiangSH/NCHU-Good-Class.git
cd NCHU-Good-Class-Dataset
```

### 2. 準備課程資料

從學校API取得課程資料，但因為有時候API回傳的json格式會錯誤(不會太多，大約2~3個)，所以要麻煩人工修正一下。

修正好後存在`/data`資料夾下，檔名為`course<semester>.json`。

`<semester>`代表學期，格式為`年度+上/下學期`，例如：110年上學期->`1101`，110年下學期->`1102`，依此類推。

### 3. 下載pandas

```
pip install pandas==1.2.4
```

### 4. 執行`export.py`

```
python export.py <semester>
```

### 5. 執行結果

執行結果存在`/data`資料夾下，會有兩個檔案，分別是課程資料`class<semester>.xlsx`以及系所資料`dept<semester>.xlsx`。

如果有需要，也可以直接修改xlsx檔案裡面的資料。

### 6. 匯入資料庫

前往[中興好課後端](https://nchugoodclass.herokuapp.com/admin/login/?next=/admin/)，並登入管理者(admin)。

登入後，點擊Class。因為我使用`django-import-export`套件，所以右上方會出現**IMPORT**和**EXPORT**按鈕。

![](https://i.imgur.com/CKNJCCp.png)

匯入選擇**IMPORT**，匯入先前產生的`class<semester>.xlsx`，格式選擇`xlsx`，完成後點**SUBMIT**。

如果出現錯誤，請檢查`class<semester>.xlsx`中是否具有上述欄位。

![](https://i.imgur.com/hwJz44v.png)

接著會出現一個預覽清單，請檢查資料是否正確，如果沒問題就按**Confirm import**正式匯入。

因為資料量多，匯入會需要比較久的時間，這段時間請不要關閉瀏覽器或斷開網路，避免資料出現錯誤。

匯入成功後即可在Class中看到匯入的課程，匯入系所也是同樣的方法。

### 7. 驗證

到[中興好課 - 課程清單](https://nchugoodclass.herokuapp.com/web/class/)檢查課程資料是否成功更新。


## 作者

* 江尚軒([@AndyChiangSH](https://github.com/AndyChiangSH))
