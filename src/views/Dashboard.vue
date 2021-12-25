<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card shadow="hover"
                 class="mgb20"
                 style="height:252px;">
          <div class="user-info">
            <img src="../assets/img/img.jpg"
                 class="user-avator"
                 alt />
            <div class="user-info-cont">
              <div class="user-info-name">{{ name }}</div>
              <div>{{ role }}</div>
            </div>
          </div>
          <div class="user-info-list">
            上次登录时间：
            <span>2021-12-13</span>
          </div>
          <div class="user-info-list">
            上次登录地点：
            <span>北京</span>
          </div>
        </el-card>
        <el-card shadow="hover"
                 style="height:252px;">
          <template #header>
            <div class="clearfix">
              <span>语言详情</span>
            </div>
          </template>
          Vue
          <el-progress :percentage="45.5"
                       color="#42b983"></el-progress>python
          <el-progress :percentage="42.3"
                       color="#f1e05a"></el-progress>JavaScript
          <el-progress :percentage="8.1"></el-progress>CSS
          <el-progress :percentage="3.4"
                       color="#f56c6c"></el-progress>
        </el-card>
      </el-col>
      <el-col :span="16">
        <el-row :gutter="20"
                class="mgb20">
          <el-col :span="8">
            <el-card shadow="hover"
                     :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-1">
                <i class="el-icon-user-solid grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">10532</div>
                  <div>用户总数</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover"
                     :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-2">
                <i class="el-icon-video-camera-solid grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">58098</div>
                  <div>电影总数</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover"
                     :body-style="{ padding: '0px' }">
              <div class="grid-content grid-con-3">
                <i class="el-icon-s-flag grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">1128</div>
                  <div>标签数量</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-card shadow="hover"
                 style="height:403px;">
          <template #header>
            <div class="clearfix">
              <span>待办事项</span>
              <el-button style="float: right; padding: 3px 0"
                         type="text">添加</el-button>
            </div>
          </template>

          <el-table :show-header="false"
                    :data="todoList"
                    style="width:100%;">
            <el-table-column width="40">
              <template #default="scope">
                <el-checkbox v-model="scope.row.status"></el-checkbox>
              </template>
            </el-table-column>
            <el-table-column>
              <template #default="scope">
                <div class="todo-item"
                     :class="{
                                        'todo-item-del': scope.row.status,
                                    }">{{ scope.row.title }}</div>
              </template>
            </el-table-column>
            <el-table-column width="60">
              <template>
                <i class="el-icon-edit"></i>
                <i class="el-icon-delete"></i>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card shadow="hover">
          <schart ref="bar"
                  class="schart"
                  canvasId="bar"
                  :options="options"></schart>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card shadow="hover">
          <schart ref="line"
                  class="schart"
                  canvasId="line"
                  :options="options2"></schart>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Schart from "vue-schart";
import { reactive } from "vue";
export default {
  name: "dashboard",
  components: { Schart },
  setup () {
    const name = localStorage.getItem("ms_username");
    const role = name === "admin" ? "超级管理员" : "普通用户";

    const options = {
      type: "bar",
      title: {
        text: "各类别电影数量表1",
      },
      xRorate: 25,
      labels: ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime'],
      datasets: [
        {
          label: "电影数量",
          data: [4067, 2663, 2749, 15956, 2637, 7412, 24144, 7130, 5105],
        }
      ],
    };
    const options2 = {
      type: "line",
      title: {
        text: "各类别电影数量表2",
      },
      labels: ['Thriller', 'Horror', 'Mystery', 'Sci-Fi', 'IMAX', 'Documentary', 'War', 'Musical', 'Western', 'Film-Noir'],
      datasets: [
        {
          label: "电影数量",
          data: [8216, 5555, 2773, 3444, 197, 5118, 1820, 1113, 1378, 364],
        },
      ],
    };
    const todoList = reactive([
      {
        title: "MySQL,mongodb导入数据并优化",
        status: true,
      },
      {
        title: "python链接数据库,编写4个功能接口",
        status: true,
      },
      {
        title: "搭建vue框架,写好样式并接入接口",
        status: true,
      },
      {
        title: "调试完成,打包放入服务器",
        status: true,
      },
      {
        title: "服务器调试,配置tomcat和nginx",
        status: true,
      },
      {
        title: "配置域名访问,解决跨域问题",
        status: true,
      },
    ]);

    return {
      name,
      options,
      options2,
      todoList,
      role,
    };
  },
};
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
  color: rgb(242, 94, 67);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

.mgb20 {
  margin-bottom: 20px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}

.schart {
  width: 100%;
  height: 300px;
}
</style>
