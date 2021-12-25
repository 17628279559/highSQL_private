import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    redirect: '/dashboard',
    component: Home,
    children: [
      {
        path: "/dashboard",
        name: "dashboard",
        meta: {
          title: '系统首页'
        },
        component: () => import("../views/Dashboard.vue")
      }, {
        path: "/idselect",
        name: "idselect",
        exact: true,
        meta: {
          title: 'ID查询'
        },
        component: () => import("../views/BaseTable.vue")
      }, {
        path: '/keyselect',
        name: 'keyselect',
        exact: true,
        meta: {
          title: '关键词查询'
        },
        component: () => import('../views/BaseKey.vue')
      }, {
        path: '/top',
        name: 'top',
        exact: true,
        meta: {
          title: 'top风格查询'
        },
        component: () => import('../views/BaseTop.vue')
      }, {
        path: '/gender',
        name: 'gender',
        exact: true,
        meta: {
          title: '性别推荐'
        },
        component: () => import('../views/BaseGender.vue')
      },
    ]
  }, {
    path: "/login",
    name: "Login",
    exact: true,
    meta: {
      title: '登录'
    },
    component: () => import("../views/Login.vue")
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} | vue-manage-system`;
  const role = localStorage.getItem('ms_username');
  if (!role && to.path !== '/login') {
    next('/login');
  } else if (to.meta.permission) {
    // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
    role === 'admin'
      ? next()
      : next('/403');
  } else {
    next();
  }
});

export default router;