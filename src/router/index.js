import {createRouter, createWebHashHistory} from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    {
        path: '/',
        redirect: '/dashboard'
    }, {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: "/dashboard",
                name: "dashboard",
                meta: {
                    title: '系统首页'
                },
                component: () => import (  "../views/Dashboard.vue")
            }, {
                path: "/IDselect",
                name: "idselect",
                meta: {
                    title: 'ID查询'
                },
                component: () => import (  "../views/BaseTable.vue")
            }, {
                path: '/KEYselect',
                name: 'keyselect',
                meta: {
                    title: '关键词查询'
                },
                component: () => import ( '../views/BaseKey.vue')
            },{
                path: '/Top',
                name: 'top',
                meta: {
                    title: 'top风格查询'
                },
                component: () => import ( '../views/BaseTop.vue')
            },{
                path: '/Gender',
                name: 'gender',
                meta: {
                    title: '性别推荐'
                },
                component: () => import ( '../views/BaseGender.vue')
            },{
                path: '/404',
                name: '404',
                meta: {
                    title: '找不到页面'
                },
                component: () => import ( '../views/404.vue')
            }, 
			
        ]
    }, {
        path: "/login",
        name: "Login",
        meta: {
            title: '登录'
        },
        component: () => import (  "../views/Login.vue")
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