# -*- coding: utf-8 -*-


import json
import string
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.write("Hello, world")
        

class CandidatesRecommendationHandler(tornado.web.RequestHandler):
    
    def post(self):
        sat = self.get_argument("sat")
        toefl = self.get_argument("toefl")
        discipline = self.get_argument("discipline")
        school_list = self.__get_school_list()
        json_result = self.__generate_json(school_list)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json_result)
        
    def __generate_json(self, result):
        json_result = {}
        json_result["result"] = result
        json_result["error"] = 0
        json_result["description"] = "No error"
        return json.dumps(json_result)
    
    def __get_school_list(self):
        list = []
        school_info1 = {}
        school_info1["id"] = 1
        school_info1["name"] = "哈佛大学"
        school_info1["rate"] = "80%"
        school_info2 = {}
        school_info2["id"] = 2
        school_info2["name"] = "麻省理工学院"
        school_info2["rate"] = "70%"
        school_info3 = {}
        school_info3["id"] = 3
        school_info3["name"] = "吉林大学"
        school_info3["rate"] = "69%"
        list.append(school_info1)
        list.append(school_info2)
        list.append(school_info3)
        return list
        
class SchoolInfosHandler(tornado.web.RequestHandler):
    
    def get(self):
        school_list = self.__get_school_list()
        json_result = self.__generate_json(school_list)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json_result)
        
    def __generate_json(self, result):
        json_result = {}
        json_result["result"] = result
        json_result["error"] = 0
        json_result["description"] = "No error"
        return json.dumps(json_result)
        
    def __get_school_list(self):
        list = []
        school_info1 = {}
        school_info1["id"] = 1
        school_info1["name"] = "哈佛大学"
        school_info1["englishName"] = "HARVARD"
        school_info1["sat"] = 100
        school_info1["toefl"] = 110
        school_info2 = {}
        school_info2["id"] = 2
        school_info2["name"] = "麻省理工学院"
        school_info2["englishName"] = "MIT"
        school_info2["sat"] = 100
        school_info2["toefl"] = 100
        school_info3 = {}
        school_info3["id"] = 3
        school_info3["name"] = "吉林大学"
        school_info3["englishName"] = "JLU"
        school_info3["sat"] = 90
        school_info3["toefl"] = 90
        list.append(school_info1)
        list.append(school_info2)
        list.append(school_info3)
        return list
        
        
class SchoolInfoHandler(tornado.web.RequestHandler):
    
    def get(self, school_id):
        school_info = self.__get_school_info(string.atoi(school_id))
        json_result = self.__generate_json(school_info)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json_result)
        
    def __generate_json(self, result):
        json_result = {}
        json_result["result"] = result
        json_result["error"] = 0
        json_result["description"] = "No error"
        return json.dumps(json_result)
        
    def __get_school_info(self, id):
        if 1 == id:
            return self.__get_1_school_info()
        elif 2 == id:
            return self.__get_2_school_info()
        elif 3 == id:
            return self.__get_3_school_info()
        
    def __get_1_school_info(self):
        school_info = {}
        school_info["schoolID"] = 1
        school_info["schoolName"] = "哈佛大学"
        school_info["schoolProfile"] = "一大堆情况介绍"
        school_info["admissionStatus"] = "一大堆文字"
        return school_info
    
    def __get_2_school_info(self):
        school_info = {}
        school_info["schoolID"] = 2
        school_info["schoolName"] = "麻省理工学院"
        school_info["schoolProfile"] = "两大堆情况介绍"
        school_info["admissionStatus"] = "两大堆文字"
        return school_info
    
    def __get_3_school_info(self):
        school_info = {}
        school_info["schoolID"] = 3
        school_info["schoolName"] = "吉林大学"
        school_info["schoolProfile"] = "三大堆情况介绍"
        school_info["admissionStatus"] = "三大堆文字"
        return school_info
    

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/schoolinfo/([0-9]+)", SchoolInfoHandler),
    (r"/schoolinfos", SchoolInfosHandler),
    (r"/candidatesrecommendation", CandidatesRecommendationHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()