from manim import *

# Video_1 e Video_2 foram as primeiras feitas, só de partes da seção 3-2
# class Video_1(Scene):
#     def construct(self):
#         linguagem = MathTex(
#             r"{{L =}} "
#             r"\{",
#             r"{{ 10 }},",
#             r"{{ 11 }},",
#             r"{{ 101 }},",
#             r"{{ 111 }}",
#             r"\}"
#         )
#         self.play(Write(linguagem[1:]), run_time=3)
#         self.play(Write(linguagem[0]))
#         self.play(linguagem.animate.shift(1.5*UP))

#         maquina = Square().next_to(linguagem, DOWN, buff=1.5).set_fill(BLACK, opacity=1.0)

#         self.play(Create(maquina))
#         self.add_foreground_mobjects(maquina)

#         a = MathTex(r"{{ 101 }}")
#         a.next_to(maquina, LEFT, buff=0.5)
#         # self.bring_to_front(maquina)

#         self.play(FadeIn(a, target_position=linguagem[5]))
#         self.play(FadeOut(a, target_position=maquina))

#         y = Tex(r"{{sim}}")
#         y.next_to(maquina, RIGHT, buff=0.5)
#         self.bring_to_back(y)

#         self.play(FadeIn(y, target_position=maquina))
#         self.wait(2)

#         self.play(FadeOut(y))
#         self.wait(1)

#         b = MathTex(r"{{ 100 }}")
#         b.next_to(maquina, LEFT, buff=0.5)
#         # self.bring_to_front(maquina)

#         self.play(FadeIn(b))
#         self.wait(1)
#         self.play(FadeOut(b, target_position=maquina))

#         n = Tex(r"{{não}}")
#         n.next_to(maquina, RIGHT, buff=0.5)
#         self.bring_to_back(n)

#         self.play(FadeIn(n, target_position=maquina))
#         self.wait(2)

# class Video_2(Scene):
#     def construct(self):
#         # limitante = MathTex(
#         #     r"T_M(n) \in O(n^k) \\",
#         #     r"\iff \\",
#         #     r"\exists c\inT_M(n)"
#         # )
#         # assintotica = MathTex(
#         #     r"f(n) \in O(g(n)) \\",
#         #     r"\iff \\",
#         #     r"\exists c, N f(n) \leq c g(n) \forall n \geq N"
#         # )
#         assintotica = [MathTex(s).shift((1 - i) * UP) for i, s in enumerate([
#             r"f(n) \in O(g(n))",
#             r"\iff",
#         ])]
#         assintotica.append(MathTex(r"\exists c, N \text{ tais que } f(n) \leq c g(n) \text{, } \forall n \geq N").shift(DOWN))

#         re = FullScreenRectangle()
#         note = Tex(r"(sendo f e g funções assintoticamente não-negativas)")
#         note.next_to(re.get_bottom(), UP)

#         self.play(*(FadeIn(a) for a in assintotica))
#         self.wait(3.5)

#         self.play(FadeIn(note))
#         self.wait(4.5)
#         self.play(FadeOut(note))

#         novo1 = MathTex(r"T_M(n) \in O(n^k)").shift(UP)
#         novo2 = MathTex(r"\exists c, N \text{ tais que } f(n) \leq c n^k \text{, } \forall n \geq N").shift(DOWN)

#         self.play(
#             TransformMatchingShapes(assintotica[0], novo1),
#             TransformMatchingShapes(assintotica[2], novo2)
#         )
#         self.wait(4)
        
#         novo3 = MathTex(r"T_M(n) \in O(2^{n^k})").shift(3*DOWN/2 + DOWN/6)
#         novo1.generate_target()
#         novo1.target.move_to(ORIGIN + UP/2 + UP/6)

#         novo4 = Tex(r"Polinomial").next_to(novo1.target, UP, buff=0.4)
#         novo5 = Tex(r"Exponencial").next_to(novo3, UP)
#         self.play(
#             MoveToTarget(novo1),
#             FadeIn(novo3),
#             FadeIn(novo4),
#             FadeIn(novo5),
#             FadeOut(novo2),
#             FadeOut(assintotica[1]),
#         )
#         self.wait(4)

#         # ImageMobject('path')

class Audio1(Scene):
    def construct(self):
        self.wait(14.5)
        self.wait(30.7 - 14.5)
        img = ImageMobject('alanturing.webp', scale_to_resolution=1501).scale(0.75)
        alan = Tex("Alan Turing (1912-1954)").next_to(img, DOWN, buff=0.25)
        self.play(FadeIn(img), FadeIn(alan), run_time=0.5)
        self.wait(46.5 - 31.2)
        self.play(FadeOut(img), FadeOut(alan), run_time=0.3)
        mm = Tex("Máquinas de Turing").shift(3*UP)
        sq = Square().set_fill(BLACK, opacity=1.0)
        m = Tex("M")
        maquina = Group(sq, m)
        self.play(FadeIn(mm), FadeIn(maquina), run_time=0.4)
        self.wait(52.6 - 47.2)
        self.wait(57.4 - 52.6)
        det = Tex("Determinísticas")
        ndet = Tex("Não determinísticas")
        maquina2 = Group(sq.copy(), Tex("N"))
        det.next_to(maquina, UP, buff=1.0)
        ndet.next_to(maquina2, UP, buff=1.0)
        g1 = Group(maquina, det)
        g2 = Group(maquina2, ndet)
        tg = Group(g1, g2)
        tg.arrange(buff=1.0)
        self.play(FadeIn(tg), run_time=0.4)
        self.wait(75.5 - 57.8)
        self.clear()
        self.wait(77.0 - 75.5)
        pnp = Tex("Classes P e NP").shift(3*UP)
        p = Tex("P").scale(1.8).shift(1.5*UP + 2.25*LEFT)
        np = Tex("NP").scale(1.8).shift(1.5*UP + 2.25*RIGHT)
        self.play(FadeIn(pnp), FadeIn(p), FadeIn(np), run_time=0.3)
        self.wait(99 - 77.3)
        sm = Tex("Super Mario").next_to(np, DOWN, buff=0.5)
        self.play(FadeIn(sm), run_time=0.4)
        self.wait(103.8 - 99.4)
        tlp = Tex("Caixeiro viajante").next_to(sm, DOWN, buff=0.3)
        primes = Tex("Teste de primalidade").next_to(p, DOWN, buff=0.5)
        mo = Tex("Muitos outros").next_to(primes, DOWN, buff=0.3)
        mo2 = Tex("Muitos outros").next_to(tlp, DOWN, buff=0.3)
        self.play(FadeIn(tlp), FadeIn(primes), FadeIn(mo), FadeIn(mo2), run_time=0.4)
        self.wait(110.7 - 104.2)
        self.play(FadeOut(pnp), FadeOut(p), FadeOut(np), FadeOut(sm), FadeOut(tlp), FadeOut(primes), FadeOut(mo), FadeOut(mo2), run_time=0.2)
        self.wait(0.1)
        neq = MathTex(r"\neq").scale(1.8)
        p.move_to(ORIGIN)
        np.move_to(ORIGIN)
        g4 = Group(p, neq, np).arrange(buff=0.35)
        self.play(FadeIn(g4), run_time=0.3)
        self.wait(115.4 - 111.3)
        nneq = MathTex(r"\stackrel{?}{\neq}").scale(1.8)
        g5 = Group(p, nneq, np).arrange(buff=0.35)
        nneq.shift(0.3*UP)
        self.play(TransformMatchingShapes(g4, g5))
        self.wait(160 - 115.4)



class Audio3_2(Scene):
    def construct(self):
        self.wait(12.3)
        ling = Tex("Linguagens").shift(2.5*UP)
        self.play(FadeIn(ling), run_time=0.6)
        self.wait(13.5 - 12.9)
        linguagem = MathTex(
            r"{{L =}} "
            r"\{",
            r"{{ 10 }},",
            r"{{ 11 }},",
            r"{{ 101 }},",
            r"{{ 111 }},",
            r"{{ \dots }}"
            r"\}"
        )
        self.play(Write(linguagem[0]), Write(linguagem[1]), Write(linguagem[-1]), run_time=1)
        self.wait(1)
        self.play(Write(linguagem[2:-1]), run_time=1.5)
        self.wait(28.1 - 17.0)
        mod = Tex("Modelos de Computação").shift(2.5*UP)
        self.play(Transform(ling, mod), run_time=0.9)
        self.wait(38.0 - 29.0)
        self.play(linguagem.animate.shift(1.5*UP), run_time=2)
        self.wait(40.0 - 38.0)
        msq = Square().set_fill(BLACK, opacity=1.0)
        mtex = Tex("M").scale(1.5)
        maquina = Group(msq, mtex).next_to(linguagem, DOWN, buff=1.5)
        self.play(Create(msq), Write(mtex), run_time=0.5)
        self.add_foreground_mobjects(msq)
        self.add_foreground_mobjects(mtex)

        a = MathTex(r"{{ 101 }}")
        a.next_to(maquina, LEFT, buff=0.5)
        # self.bring_to_front(maquina)

        self.wait(0.75)
        self.play(FadeIn(a, target_position=linguagem[5]), run_time=0.25)
        self.play(FadeOut(a, target_position=maquina), run_time=0.5)

        y = Tex(r"{{sim}}")
        y.next_to(maquina, RIGHT, buff=0.5)
        self.bring_to_back(y)

        self.play(FadeIn(y, target_position=maquina), run_time=0.5)
        self.wait(0.25)

        self.play(FadeOut(y), run_time=0.5)
        self.wait(0.25)

        b = MathTex(r"{{ 100 }}")
        b.next_to(maquina, LEFT, buff=0.5)
        # self.bring_to_front(maquina)

        self.play(FadeIn(b), run_time=0.25)
        self.play(FadeOut(b, target_position=maquina), run_time=0.5)

        n = Tex(r"{{não}}")
        n.next_to(maquina, RIGHT, buff=0.5)
        self.bring_to_back(n)

        self.play(FadeIn(n, target_position=maquina), run_time=0.5)
        self.wait(0.25)

        self.play(FadeOut(n), run_time=0.5)
        self.wait(55.6 - 47.5)

        tese = Tex("Tese de Church-Turing")
        self.play(Transform(maquina, tese), Uncreate(ling), Uncreate(linguagem), run_time=0.8)
        self.wait(0.5)
        iguais = Tex("Os modelos são todos equivalentes")
        self.play(maquina.animate.shift(2.0*UP), Write(iguais), run_time=0.8)

        self.wait(70.5 - 57.7)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.5)

        self.wait(79.5 - 71.0)
        tm = MathTex(r"T_M").scale(1.1)
        self.play(FadeIn(tm), run_time=1)
        self.wait(85.2 - 80.5)

        s = MathTex(r"x \gets \text{string}, n = |x|").shift(UP*1.2)
        ntm = MathTex(r"T_M(n)").scale(1.1)
        self.play(FadeIn(s), TransformMatchingShapes(tm, ntm), run_time=0.8)

        self.wait(89.5 - 86.0)
        self.play(FadeOut(s), run_time=0.6)
        self.wait(90.7 - 90.1)

        # assintotica = [MathTex(s).shift((1 - i) * UP) for i, s in enumerate([
        #     r"f(n) \in O(g(n))",
        #     r"\iff",
        # ])]
        # assintotica.append(MathTex(r"\exists c, N \text{ tais que } f(n) \leq c g(n) \text{, } \forall n \geq N").shift(DOWN))

        # re = FullScreenRectangle()
        # note = Tex(r"(sendo f e g funções assintoticamente não-negativas)")
        # note.next_to(re.get_bottom(), UP)

        # self.play(*(FadeIn(a) for a in assintotica))
        # self.wait(3.5)

        # self.play(FadeIn(note))
        # self.wait(4.5)
        # self.play(FadeOut(note))

        poly = Tex("Tempo polinomial").scale(1.1).shift(2.25*UP)
        novo1 = MathTex(r"{{T_M(n) \in O(}}{{n^k}}{{)}}").shift(UP)
        iff = MathTex(r"\Leftrightarrow")
        novo2 = MathTex(r"{{\exists c, N \text{ tais que } T_M(n) \leq c}} {{n^k}} {{\text{, } \forall n \geq N}}").shift(DOWN)
        self.play(FadeIn(poly), TransformMatchingShapes(ntm, novo1), FadeIn(iff), FadeIn(novo2), run_time=0.6)

        self.wait(118.6 - 91.3)

        exp = Tex("Tempo exponencial").scale(1.1).shift(2.25*UP)
        novo3 = MathTex(r"{{T_M(n) \in O(}}2^{{{n^k}}}{{)}}").shift(UP)
        novo4 = MathTex(r"{{\exists c, N \text{ tais que } T_M(n) \leq c }} 2^{{{n^k}}} {{\text{, } \forall n \geq N}}").shift(DOWN)
        self.play(TransformMatchingTex(novo1, novo3), TransformMatchingTex(novo2, novo4), Transform(poly, exp), run_time=0.8)

        self.wait(127.7 - 119.4)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.5)
        diagrama = ImageMobject('diagrama_pnp_v2.png', scale_to_resolution=346).scale(0.75)
        self.play(FadeIn(diagrama), run_time=0.5)

        self.wait(154.0 - 128.7)

        self.play(FadeOut(diagrama), run_time=0.5)
        self.wait(0.3)
        sat = Tex("Satisfatibilidade booleana (SAT)").scale(1.1).shift(2.5*UP)
        self.play(FadeIn(sat), run_time=0.8)

        formula = MathTex(
            r"\varphi", r"=",
            r"(", r"x_1", r"\lor", r"x_2", r"\lor", r"\neg", r"x_3", r")",
            r"\land",
            r"(", r"\neg", r"x_1", r"\lor", r"x_5", r"\land", r"\neg", r"x_4", r"\land", r"x_2", r")",
            r"\lor",
            r"\neg", r"(", r"x_2", r"\lor", r"x_3", r")"
        ).shift(UP)
        
        self.wait(157.6 - 155.6)
        self.play(*[FadeIn(formula[i]) for i in [0]], run_time=0.4)
        self.wait(159.2 - 158.0)
        self.play(*[FadeIn(formula[i]) for i in [10, 16, 19]], run_time=0.4)
        self.wait(160.2 - 159.6)
        self.play(*[FadeIn(formula[i]) for i in [4, 6, 14, 22, 26]], run_time=0.4)
        self.wait(161.0 - 160.6)
        self.play(*[FadeIn(formula[i]) for i in [7, 12, 17, 23]], run_time=0.4)
        self.wait(162.0 - 161.4)
        self.play(*[FadeIn(formula[i]) for i in [1, 2, 3, 5, 8, 9, 11, 13, 15, 18, 20, 21, 24, 25, 27, 28]], run_time=0.4)
        self.wait(165.1 - 162.4)

        valoracao = MathTex(
            r"x_1 = ", r"1", r"\\",
            r"x_2 = ", r"1", r"\\",
            r"x_3 = ", r"0", r"\\",
            r"x_4 = ", r"0", r"\\",
            r"x_5 = ", r"1"
        ).next_to(formula, DOWN, buff=0.5)
        self.play(*[FadeIn(valoracao[i]) for i in [0, 2, 3, 5, 6, 8, 9, 11, 12]], run_time=0.4)
        self.wait(172.6 - 165.5)
        self.play(*[FadeIn(valoracao[i]) for i in [1, 4, 7, 10, 13]], run_time=0.4)

        self.wait(176.9 - 173.0)
        subst = MathTex(
            r"\varphi", r"=",
            r"(", r"1", r"\lor", r"1", r"\lor", r"\neg", r"0", r")",
            r"\land",
            r"(", r"\neg", r"1", r"\lor", r"1", r"\land", r"\neg", r"0", r"\land", r"1", r")",
            r"\lor",
            r"\neg", r"(", r"1", r"\lor", r"0", r")"
        ).shift(UP)
        self.play(TransformMatchingShapes(formula, subst), run_time=0.5)
        verdadeira = MathTex(r"\varphi = 1").shift(UP)
        self.wait(178.0 - 177.4)
        self.play(TransformMatchingShapes(subst, verdadeira), FadeOut(valoracao), run_time=0.5)
        self.wait(182.1 - 178.5)

        satcompleto = Tex("SAT é NP-completo").shift(UP)
        self.play(ReplacementTransform(verdadeira, satcompleto), FadeOut(sat), run_time=0.5)
        self.wait(0.3)
        self.play(satcompleto.animate.shift(1.4*UP), run_time=0.5)

        self.wait(185.1 - 183.4)
        red = MathTex(r"\forall L \in \mathrm{NP},\,\, \exists R").shift(0.4*UP)
        redd= MathTex(r"L \prec_R \mathrm{SAT}").next_to(red, DOWN, buff=0.4)
        self.play(Write(red), Write(redd), run_time=0.5)

        self.wait(214.7 - 185.6)
        cook_levin = Tex("Teorema de Cook-Levin:").shift(2.2*UP)
        self.play(FadeIn(cook_levin), satcompleto.animate.shift(1.2*DOWN), red.animate.shift(0.7*DOWN), redd.animate.shift(0.7*DOWN), run_time=0.8)

        self.wait(227.9 - 215.5)



        # self.play(
        #     TransformMatchingShapes(assintotica[0], novo1),
        #     TransformMatchingShapes(assintotica[2], novo2)
        # )
        # self.wait(4)
        
        # novo3 = MathTex(r"T_M(n) \in O(2^{n^k})").shift(3*DOWN/2 + DOWN/6)
        # novo1.generate_target()
        # novo1.target.move_to(ORIGIN + UP/2 + UP/6)

        # novo4 = Tex(r"Polinomial").next_to(novo1.target, UP, buff=0.4)
        # novo5 = Tex(r"Exponencial").next_to(novo3, UP)
        # self.play(
        #     MoveToTarget(novo1),
        #     FadeIn(novo3),
        #     FadeIn(novo4),
        #     FadeIn(novo5),
        #     FadeOut(novo2),
        #     FadeOut(assintotica[1]),
        # )
        # self.wait(4)


class Audio2(Scene):
    def construct(self):
        self.wait(2.0)
        hist_compx = Tex("História da Complexidade Computacional").shift(1.8*UP)
        self.play(FadeIn(hist_compx), run_time=0.5)
        self.wait(15.5 - 2.5)
        algs = Tex("Algoritmos")
        self.play(FadeIn(algs), run_time=0.5)
        self.wait(31 - 16)
        teo_bilidade = Tex("Teoria da Computabilidade")
        self.play(ReplacementTransform(algs, teo_bilidade), run_time=0.75)
        self.wait(0.5)
        self.play(FadeOut(hist_compx), teo_bilidade.animate.shift(1.8*UP), run_time=0.75)
        self.wait(50 - 33)
        hilbert = ImageMobject('davidhilbert.jpg', scale_to_resolution=738).scale(0.75)
        hil_label = Tex("David Hilbert (1862-1943)").next_to(hilbert, DOWN, buff=0.2)
        self.play(FadeIn(hilbert), FadeIn(hil_label), teo_bilidade.animate.shift(1.5*UP), run_time=0.5)
        self.wait(70.0 - 50.5)
        self.play(FadeOut(hilbert), FadeOut(hil_label), run_time=0.4)
        self.wait(0.2)
        church_i = ImageMobject('alonzochurch.jpg', scale_to_resolution=909).scale(0.75)
        chu_label = Tex("Alonzo Church (1903-1995)").next_to(church_i, DOWN, buff=0.2)
        church = Group(church_i, chu_label)

        turing_i = ImageMobject('alanturing.webp', scale_to_resolution=1501).scale(0.75)
        tur_label = Tex("Alan Turing (1912-1954)").next_to(turing_i, DOWN, buff=0.2)
        turing = Group(turing_i, tur_label)

        both = Group(church, turing).arrange().shift(0.4*DOWN)
        self.play(FadeIn(church), run_time=0.4)
        self.play(FadeIn(turing), run_time=0.4)
        self.wait(89.5 - 71.4)
        self.play(FadeOut(church), FadeOut(turing), run_time=0.4)
        self.wait(0.1)
        
        lambda_c = Tex(r"Cálculo\\", "Lambda")
        equiv = MathTex(r"\equiv")
        maquina_t = Tex(r"Máquinas\\", "de Turing")

        coisas = Group(lambda_c, equiv, maquina_t).arrange()
        self.play(FadeIn(lambda_c), run_time=0.5)
        self.wait(2.5)
        self.play(FadeIn(maquina_t), run_time=0.5)
        self.wait(96 - 93.5)
        self.play(FadeIn(equiv), run_time=0.3)

        self.wait(108.5 - 96.3)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.5)
        parada = Tex("Problema da Parada").shift(2*UP)
        self.play(FadeIn(parada), run_time=0.5)
        self.wait(135.8 - 109.5)
        comp_trat = Tex("Computável vs Tratável").shift(2*UP)
        self.play(ReplacementTransform(parada, comp_trat), run_time=0.5)
        self.wait(171.4 - 136.3)
        temp_esp = Tex(r"Tempo gasto\\", "Espaço necessário")
        self.play(FadeIn(temp_esp), run_time=0.5)
        self.wait(178.8 - 171.9)
        teo_plex = Tex("Teoria da Complexidade Computacional").shift(2*UP)
        self.play(FadeOut(comp_trat), ReplacementTransform(temp_esp, teo_plex), run_time=0.5)
        self.wait(200.1 - 179.3)
        alg_eff = Tex(r"Algoritmo Eficiente\\", "Problemas Computacionalmente Admissíveis")
        self.play(FadeIn(alg_eff), run_time=0.5)
        self.wait(225 - 200.6)
        
        vs = Tex(" vs ").scale(1.8)
        p = Tex("P").scale(1.8)
        exp = Tex("EXP").scale(1.8)
        g4 = Group(p, vs, exp).arrange(buff=0.35)
        self.play(FadeOut(teo_plex), ReplacementTransform(alg_eff, vs), FadeIn(p), FadeIn(exp), run_time=0.5)
        self.wait(250.7 - 225.5)


class Audio3_1(Scene):
    def construct(self):
        self.wait(5.3)
        prob_comp = Tex("Problemas Computacionais").shift(UP)
        self.play(FadeIn(prob_comp), run_time=0.5)
        self.wait(9.4 - 5.8)
        conj_prob = Tex("Conjuntos de problemas").shift(DOWN)
        self.play(FadeIn(conj_prob), run_time=0.5)
        self.wait(28.4 - 9.9)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.3)
        diagrama_1 = ImageMobject('diagrama_1.png', scale_to_resolution=405).scale(0.75)
        self.play(FadeIn(diagrama_1), run_time=0.5)
        self.wait(59 - 29.2)
        self.play(FadeOut(diagrama_1), run_time=0.5)
        self.wait(60.6 - 59.5)
        diagrama = ImageMobject('diagrama_pnp_v2.png', scale_to_resolution=346).scale(0.75)
        self.play(FadeIn(diagrama), run_time=0.5)
        self.wait(70.5 - 61.1)
        self.play(FadeOut(diagrama), run_time=0.5)
        self.wait(72 - 71)


class Audio4(Scene):
    def construct(self):
        self.wait(2)
        impor = Tex("Importância de P vs NP").scale(1.3).shift(2.3*UP)
        self.play(FadeIn(impor), run_time=1)
        self.wait(20.4 - 3)
        milen = Tex("Um dos problemas do milênio")
        cript = Tex("Criptografia").next_to(milen, UP)
        resol = Tex("Resolve um, resolve todos").next_to(milen, DOWN)
        self.play(FadeIn(cript), run_time=1)
        self.wait(47.7 - 21.4)
        self.play(FadeIn(milen), run_time=1)
        self.wait(66.8 - 48.7)
        self.play(FadeIn(resol), run_time=1)
        self.wait(90.8 - 67.8)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.3)
        humaq = Tex("Humanos vs Máquinas").scale(1.2).shift(2*UP)
        self.play(FadeIn(humaq), run_time=1)
        humaq.generate_target()
        humaq.target.move_to(ORIGIN).scale(2)
        self.play(MoveToTarget(humaq), run_time=(154.8 - 91.8))
        # self.wait(154.8 - 91.8)


class Audio5(Scene):
    def construct(self):
        self.wait(1.1)
        casos3 = Tex("Caso P=NP (3 opções)").scale(1.4).shift(1.6*UP)
        self.play(FadeIn(casos3), run_time=1)
        self.wait(58.5 - 2.1)
        casosb = Tex(r"Caso P=NP e foi encontrado\\", "algoritmo eficiente").scale(1.4).shift(1.2*UP)
        self.play(ReplacementTransform(casos3, casosb), run_time=1)
        self.wait(78.1 - 59.5)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.4)
        self.wait(132.9 - 78.5)


class Audio6(Scene):
    def construct(self):
        self.wait(4.1)
        posic = Tex("Posicionamento").scale(1.2).shift(1.9*UP)
        self.play(FadeIn(posic), run_time=0.5)
        self.wait(8.6 - 4.6)
        knuth_i = ImageMobject('donaldknuth.jpg', scale_to_resolution=1197).scale(0.75)
        knu_label = Tex("Donald Knuth (1938)").next_to(knuth_i, DOWN, buff=0.2)
        knuth = Group(knuth_i, knu_label)

        lipton_i = ImageMobject('richardlipton.jpg', scale_to_resolution=355).scale(0.75)
        lip_label = Tex("Richard Lipton (1946)").next_to(lipton_i, DOWN, buff=0.2)
        lipton = Group(lipton_i, lip_label)

        both = Group(knuth, lipton).arrange().shift(0.4*DOWN)
        knuth.shift(0.2*LEFT)
        lipton.shift(0.2*RIGHT)
        self.play(FadeIn(knuth), posic.animate.shift(1.5*UP), run_time=0.5)
        self.wait(12 - 9.1)
        self.play(FadeIn(lipton), run_time=0.5)
        self.wait(15.1 - 12.5)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.4)
        enque = Tex("Enquete").scale(1.3).shift(2.4*UP)
        self.play(FadeIn(enque), run_time=0.3)

        diff = MathTex(r"\text{P}\mathbin{\neq}\text{NP}").next_to(enque, DOWN, buff=0.7).shift(1.1*RIGHT)
        extra = MathTex(r"\text{P}=\text{NP}").next_to(enque, DOWN, buff=0.7).shift(1.1*LEFT).align_to(diff, DOWN)
        igual = MathTex(r"\text{P}=\text{NP}").next_to(enque, DOWN, buff=0.7).shift(1.1*LEFT).shift(0.02*DOWN)
        self.play(FadeIn(igual), FadeIn(diff), run_time=0.3)
        self.wait(18.5 - 16.1)
        
        re = FullScreenRectangle()
        diff2002 = Tex("61").next_to(diff, DOWN, buff=0.6)
        igual2002 = Tex("9").next_to(extra, DOWN, buff=0.6)
        two002 = Tex("2002:").next_to(igual2002, LEFT, buff=1.1)
        self.play(Write(two002), run_time=0.5)
        self.wait(19.7 - 19.0)

        self.play(Write(diff2002), run_time=0.3)
        self.wait(22.7 - 20.0)
        self.play(Write(igual2002), run_time=0.3)
        self.wait(25.7 - 23.0)
        diff2012 = Tex("126").next_to(diff2002, DOWN, buff=0.5)
        igual2012 = Tex("9").next_to(igual2002, DOWN, buff=0.5)
        two012 = Tex("2012:").next_to(igual2012, LEFT, buff=1.1)
        self.play(Write(two012), run_time=0.5)
        self.wait(26.9 - 26.2)

        self.play(Write(diff2012), run_time=0.3)
        self.wait(30.0 - 27.2)
        self.play(Write(igual2012), run_time=0.3)
        self.wait(49.8 - 30.3)
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.4)
        compl = Tex("Significado de Completude").scale(1.4).shift(1.6*UP)
        self.play(FadeIn(compl), run_time=0.5)
        self.wait(72.3 - 50.7)
        self.play(FadeOut(compl), run_time=0.5)
        self.wait(75.3 - 72.8)
        n_sab = Tex("Não sabemos").scale(1.4).shift(1.4*UP)
        self.play(FadeIn(n_sab), run_time=0.5)
        self.wait(85.4 - 75.8)
        self.play(FadeOut(n_sab), run_time=0.5)
        self.wait(94.4 - 85.9)
        outras = Tex("Outras provas demoraram para sair").scale(1.2).shift(1.4*UP)
        self.play(FadeIn(outras), run_time=0.5)
        self.wait(100.8 - 94.9)
        self.play(FadeOut(outras), run_time=0.5)
        self.wait(103 - 101.3)
        # vs = Tex(" vs ").scale(1.8)
        # p = Tex("P").scale(1.8)
        # np = Tex("NP").scale(1.8)
        # g4 = Group(p, vs, np).arrange(buff=0.35)
        g4 = Tex("P vs NP").scale(1.8)
        self.play(FadeIn(g4), run_time=0.5)
        self.wait(127 - 103.5)

class Audio7(Scene):
    def construct(self):
        encerramento = Tex("Encerramento").scale(1.4).shift(1.6*UP)
        self.play(FadeIn(encerramento), run_time=2)
        self.wait(15.5 - 2.0)
        obrigado = Tex("Obrigado!").scale(1.1)
        self.play(FadeIn(obrigado), run_time=1.5)
        self.wait(19 - 17)