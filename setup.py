from setuptools import setup
import os
def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )
def find_packages(path, base="" ):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

# 패키지 폴더명 작성
setup(name="hkhkhkhk", # 패키지 폴더명으로 수정
      version="0.0.1", # 버전은 처음 0.0.1 이후 증가
      url="http://github.com/hyokwan/hkhkhkhk", # 코드 저장한 url 정의
      license="MIT", # 기본세팅
      author="kimhyokwan", #본인정보로 수정
      author_email="haiteam@kopo.ac.kr", #본인정보로 수정
      keywords=["calendar","isoweek","listsum"], #본인정보로 수정
      description="isoweek calculation and so on", #본인정보로 수정
      packages=find_packages("."),
      install_requires=["isoweek"]) # 추가 필요패키지 정의