<template>
  <el-alert
    v-show="alertIsShow"
    :title="title"
    :type="type"
    effect="dark"
    :key="componentKey"
    show-icon
  ></el-alert>
</template>
<script>
import { ElAlert } from "element-plus";
import "element-plus/es/components/alert/style/css";
export default {
  name: "AlertCustom",
  data() {
    return {
      componentKey: 0,
    };
  },
  props: {
    alertIsShow: {
      type: Boolean,
    },
    title: {
      type: String,
    },
    type: {
      type: String,
    },
  },
  updated() {
    this.$nextTick(function() {
      // Code that will run only after the
      // entire view has been re-rendered
      //   console.log(this.alertIsShow);
      if (this.alertIsShow == true) {
        this.handleAlertClose();
      }
    });
  },
  components: { ElAlert },
  methods: {
    handleAlertClose() {
      setTimeout(() => this.$emit("close_alert"), 2000);
    },
    forceRerender() {
      this.componentKey += 1;
    },
  },
};
</script>
