<template>
  <div style="height: 95%;">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-cascades"></i> 风格TOPk查询
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="handle-box">
        <el-select v-model="value"
                   filterable
                   placeholder="请选择"
                   id="inputText"
                   style="width: 30%;">
          <el-option v-for="item in options"
                     :key="item.value"
                     :label="item.label"
                     :value="item.value">
          </el-option>
        </el-select>
        <el-button type="primary"
                   @click="adddata()"
                   style="width: 15%;">查询</el-button>
      </div>
      <el-card>
        <span id="name_">风格TOPk查询</span>
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
        <el-table-column prop="title"
                         label="电影名字"
                         width="300">
          <template #default="scope">
            <el-link :href="scope.row.url"
                     target="_blank"
                     underline="false">{{ scope.row.movie_title }}</el-link>
          </template>
        </el-table-column>
        <el-table-column prop="average_rating"
                         label="平均评分">
        </el-table-column>
        <el-table-column prop="num_of_rating"
                         label="评分人数">
        </el-table-column>
      </el-table>

    </div>
  </div>
</template>


<script>
import Axios from 'axios';
export default {
  name: "top",
  data () {
    return {
      options: [{
        value: '选项1',
        label: 'Adventure'
      }, {
        value: '选项2',
        label: 'Animation'
      }, {
        value: '选项3',
        label: 'Children'
      }, {
        value: '选项4',
        label: 'Comedy',
      }, {
        value: '选项5',
        label: 'Fantasy'
      }, {
        value: '选项6',
        label: 'Romance'
      }, {
        value: '选项7',
        label: 'Drama'
      }, {
        value: '选项8',
        label: 'Action'
      }, {
        value: '选项9',
        label: 'Crime'
      }, {
        value: '选项10',
        label: 'Thriller'
      }, {
        value: '选项11',
        label: 'Horror'
      }, {
        value: '选项12',
        label: 'Mystery'
      }, {
        value: '选项13',
        label: 'Sci-Fi'
      }, {
        value: '选项14',
        label: 'IMAX'
      }, {
        value: '选项15',
        label: 'Documentary'
      }, {
        value: '选项16',
        label: 'War'
      }, {
        value: '选项17',
        label: 'Musical'
      }, {
        value: '选项18',
        label: 'Western'
      }, {
        value: '选项19',
        label: 'Film-Noir'
      }],
      tableData: [],
      value: ''
    }
  },
  methods: {
    adddata () {
      var type_of_movie = document.getElementById("inputText").value;
      var api = "/api/genre/?type_of_movie=" + type_of_movie;
      Axios.get(api).then(response => {
        if (response.data) {
          this.tableData = response.data.data;
          var namee = document.getElementById("name_");
          namee.innerHTML = type_of_movie + "类型最受欢迎的20部电影"
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