<template>
  <div style="height: 95%;">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-cascades"></i> 关键词查询
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="handle-box">
        <el-input v-model="input"
                  placeholder="关键词"
                  id="inputText1"
                  style="width: 30%;"></el-input>
        <el-button type="primary"
                   @click="adddata()"
                   style="width: 15%;">查询</el-button>
      </div>
      <el-card>
        <span id="name_">关键词查询</span>
      </el-card>
      <el-table :data="tableData"
                height="80%"
                border
                style="width: 100%">
        <el-table-column prop="movieid"
                         label="电影ID"
                         width="75">
        </el-table-column>
        <el-table-column prop="picture"
                         label="电影图片"
                         width="135">
          <template #default="scope">
            <el-image class="pict"
                      :src="scope.row.picture"
                      :preview-src-list="[scope.row.picture]">
            </el-image>
          </template>
        </el-table-column>
        <el-table-column prop="movie_title"
                         label="电影名字">
          <template #default="scope">
            <el-link :href="scope.row.url"
                     target="_blank"
                     underline="false">{{ scope.row.title }}</el-link>
          </template>
        </el-table-column>
      </el-table>

    </div>
  </div>
</template>


<script>
import Axios from 'axios';
export default {
  name: "keyselect",
  data () {
    return {
      tableData: [],
      input: ''
    }
  },
  methods: {
    adddata () {
      var key_word = document.getElementById("inputText1").value;
      var api = "/api/keyword/?key_word=" + key_word;
      Axios.get(api).then(response => {
        if (response.data) {
          this.tableData = response.data.data;
          var namee = document.getElementById("name_");
          namee.innerHTML = "含有" + key_word + "关键词的电影有" + response.data.data.length + "个"
        }
      });
    },
  }
}
</script>

<style scoped>
.table-td-thumb {
  display: block;
  margin: auto;
  width: 50px;
  height: 201px;
}
.pict {
  display: block;
  margin: auto;
  width: 135px;
  height: 201px;
}
</style>