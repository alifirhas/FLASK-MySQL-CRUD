
![Project Image](public/images/FLASK-MC.png)

---

### Table of Contents

- [Description](#description)
    - [Technologies](#technologies)
- [How To Use](#how-to-use)
    - [Download](#download)
    - [Installation](#installation)
    - [API Reference](#api-reference)
- [References](#references)
- [Todo](#todo)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Project ini dibuat dengan tujuan mengetahui konfigurasi struktur file dan folder yang bisa dilakukan dengan Flask-RESTful dan MySQL. Proses atau logic yang berada disini akan dibuat sesederhan mungkin dengan menerapkan basic logic untuk CRUD (dan update berikutnya file logic). 

#### Technologies

- FLASK-RESTful
- MySQL

[Back To The Top](#read-me-template)

---

## How To Use

#### Download

1. Download repository pada release page [Release Page](https://github.com/alifirhas/FLASK-MySQL-CRUD/releases) untuk stable release,

2. Download repositroy menggunakan `git clone` untuk melihat pembaruan terbaru

```
git clone https://github.com/alifirhas/FLASK-MySQL-CRUD.git
```

3. atau menggunakan [zip download](https://github.com/alifirhas/FLASK-MySQL-CRUD/archive/refs/heads/master.zip) jika anda tidak menginginkan/memerlukan .git folder.

#### Installation

```text

# Setup virtual env
python3 -m virtualenv env

# Activate virtual env
source ./env/bin/activate

# Install packages
pip3 install -r requirments.txt

# Start server
python3 app.py

```

#### API Reference

```html
# User
---
- URL
    BASE/
- Method
    GET, POST, PUT, DELETE
- URL Parameter
    - GET
        None
    - POST
        {
            nama (str): nama pengguna
            username (str): username pengguna
            password (str): password pengguna
        }
    - PUT
        {
            id (id): id pengguna
            nama (str): nama pengguna
            username (str): username pengguna
            password (str): password pengguna
        }
    - DELETE
        {
            id (id): id pengguna
        }
- Sucess Response
    - GET
        {
            "objects": [
                {
                    id (id): id pengguna
                    nama (str): nama pengguna
                    username (str): username pengguna
                    password (str): password pengguna
                },
                .
                .
                .
                {
                    id (id): id pengguna
                    nama (str): nama pengguna
                    username (str): username pengguna
                    password (str): password pengguna
                },
            ]
        }
    - POST
        {
            id (id): id pengguna
            nama (str): nama pengguna
            username (str): username pengguna
            password (str): password pengguna
        },
    - PUT
        {
            id (id): id pengguna
            nama (str): nama pengguna
            username (str): username pengguna
            password (str): password pengguna
        },
    - DELETE
        None
```

Sampel penggunaan API ada pada file [test.py](test.py)

[Back To The Top](#read-me-template)

---

## References

- [Intermediate Usage FLASK-RESTful](https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html)
- [Format of requests and responses](https://flask-restless.readthedocs.io/en/stable/requestformat.html)

[Back To The Top](#read-me-template)

---

## Todo

- [ ] ENV Setting
- [ ] File Upload

[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) 2022 irhasalif

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- 📧 irhasalif@gmail.com
- ⚙️ GitHub: https://github.com/alifirhas
- 🎨 Portfolio: https://alifirhas.github.io
- 💼 LinkedIn: https://www.linkedin.com/in/alif-irhas-0750331b3

[Back To The Top](#read-me-template)
