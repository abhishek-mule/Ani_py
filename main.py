from manim import *
import numpy as np

class GitHubCyberAttackEnhanced(Scene):
    def construct(self):
        # Background color (dark cyberpunk)
        self.camera.background_color = "#0F1117"
        
        # Add animated background grid
        self.add_cyber_background()
        
        # Title sequence
        self.intro_sequence()
        
        # Main story
        self.show_github_platform()
        self.show_attack_sequence()
        self.show_data_breach_stats()
        self.show_defense_measures()
        self.conclusion_sequence()
    
    def add_cyber_background(self):
        """Add animated cyberpunk-style background"""
        # Create grid lines
        grid_lines = VGroup()
        for i in range(-8, 9):
            line_v = Line(UP * 4, DOWN * 4, stroke_width=0.5, color=BLUE_D, stroke_opacity=0.3)
            line_v.shift(RIGHT * i * 0.5)
            line_h = Line(LEFT * 7, RIGHT * 7, stroke_width=0.5, color=BLUE_D, stroke_opacity=0.3)
            line_h.shift(UP * i * 0.5)
            grid_lines.add(line_v, line_h)
        
        # Add subtle pulsing effect
        self.play(
            AnimationGroup(
                *[line.animate.set_stroke(opacity=0.1) for line in grid_lines],
                lag_ratio=0.01
            ),
            run_time=2,
            rate_func=there_and_back
        )
        
        # Keep grid in background
        self.add(grid_lines)
    
    def intro_sequence(self):
        """Dramatic intro with title"""
        title = Text("GITHUB CYBER ATTACK", font="Arial Bold", font_size=48, color=RED)
        subtitle = Text("Security Breach Analysis", font="Arial", font_size=24, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Glitch effect for title
        self.play(
            Write(title, run_time=1.5),
            rate_func=rush_into
        )
        self.play(
            title.animate.set_color_by_gradient(RED, ORANGE),
            FadeIn(subtitle, shift=UP),
            run_time=1
        )
        
        # Dramatic pause with pulse
        self.play(
            title.animate.scale(1.1).set_stroke(RED, 3),
            run_time=0.5,
            rate_func=there_and_back
        )
        
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP),
            run_time=0.8
        )
    
    def show_github_platform(self):
        """Show GitHub platform with animated elements"""
        # GitHub logo with glow effect
        github_logo = Circle(radius=0.8, color=WHITE, fill_opacity=0.1)
        github_text = Text("GitHub", font="Arial Bold", font_size=32, color=WHITE)
        github_group = VGroup(github_logo, github_text).to_edge(UP, buff=1)
        
        # Add glow effect
        glow = Circle(radius=1.2, color=BLUE, fill_opacity=0.05, stroke_opacity=0)
        glow.move_to(github_group.get_center())
        
        self.play(
            FadeIn(glow, scale=0.5),
            DrawBorderThenFill(github_logo),
            Write(github_text),
            run_time=1.5
        )
        
        # Add repository indicators
        repos = VGroup()
        for i in range(6):
            repo = Rectangle(width=0.8, height=0.3, color=BLUE_C, fill_opacity=0.3)
            repo.move_to(github_group.get_center() + DOWN * 2 + RIGHT * (i - 2.5) * 1.2)
            repos.add(repo)
        
        self.play(
            LaggedStartMap(FadeIn, repos, lag_ratio=0.1),
            run_time=1.5
        )
        
        self.github_elements = VGroup(github_group, glow, repos)
        self.wait(0.5)
    
    def show_attack_sequence(self):
        """Dramatic attack sequence with multiple threat vectors"""
        # Hacker silhouette
        hacker_base = Circle(radius=0.4, color=RED, fill_opacity=0.8)
        hacker_eyes = VGroup(
            Dot(radius=0.05, color=WHITE).shift(UP * 0.1 + LEFT * 0.15),
            Dot(radius=0.05, color=WHITE).shift(UP * 0.1 + RIGHT * 0.15)
        )
        hacker = VGroup(hacker_base, hacker_eyes).to_edge(LEFT, buff=1)
        
        # Malicious code streams
        code_streams = VGroup()
        for i in range(5):
            stream = VGroup()
            for j in range(8):
                code_bit = Text(
                str(np.random.choice(["0", "1", "X", "!", "@", "#"])),
                font="Courier",
                font_size=16,
                color=RED
)

                code_bit.move_to(
                    hacker.get_center() + 
                    RIGHT * (j * 0.7 + 1) + 
                    UP * (i - 2) * 0.4
                )
                stream.add(code_bit)
            code_streams.add(stream)
        
        self.play(FadeIn(hacker, shift=LEFT), run_time=0.8)
        
        # Animated attack waves
        attack_waves = VGroup()
        for i in range(3):
            wave = Arc(
                radius=1 + i * 0.7,
                start_angle=0,
                angle=PI,
                color=RED,
                stroke_width=3,
                stroke_opacity=0.6
            )
            wave.move_to(hacker.get_center())
            attack_waves.add(wave)
        
        self.play(
            LaggedStartMap(Create, attack_waves, lag_ratio=0.3),
            LaggedStartMap(FadeIn, code_streams, lag_ratio=0.1),
            run_time=2
        )
        
        # Impact effect on GitHub
        impact_flash = Circle(
            radius=2,
            color=RED,
            fill_opacity=0.3,
            stroke_opacity=0
        ).move_to(self.github_elements[0].get_center())
        
        self.play(
            impact_flash.animate.scale(0.1).set_fill(opacity=0),
            self.github_elements[0].animate.set_color(RED),
            run_time=0.5
        )
        
        self.attack_elements = VGroup(hacker, attack_waves, code_streams)
        self.wait(0.5)
    
    def show_data_breach_stats(self):
        """Enhanced data visualization with animations"""
        # Stats title
        stats_title = Text("BREACH IMPACT", font="Arial Bold", font_size=28, color=YELLOW)
        stats_title.to_edge(DOWN, buff=3)
        
        self.play(Write(stats_title), run_time=0.8)
        
        # Enhanced bar chart data
        categories = ["Code Leaks", "Credentials", "Personal Data", "API Keys", "Secrets"]
        values = [85, 67, 92, 58, 74]
        colors = [RED, ORANGE, PURPLE, BLUE, GREEN]
        
        # Create dynamic bar chart
        bars = VGroup()
        labels = VGroup()
        value_labels = VGroup()
        
        for i, (cat, val, color) in enumerate(zip(categories, values, colors)):
            # Bar
            bar = Rectangle(
                width=0.6,
                height=0,
                fill_color=color,
                fill_opacity=0.8,
                stroke_width=2,
                stroke_color=WHITE
            )
            bar.move_to(LEFT * 4 + RIGHT * i * 1.8 + UP * 0.5)
            bars.add(bar)
            
            # Category label
            label = Text(cat, font_size=16, color=WHITE)
            label.rotate(PI/4)
            label.next_to(bar, DOWN, buff=0.3)
            labels.add(label)
            
            # Value label
            val_label = Text(f"{val}%", font_size=20, color=WHITE, weight=BOLD)
            val_label.next_to(bar, UP, buff=0.1)
            value_labels.add(val_label)
        
        # Animate bars growing with staggered effect
        self.play(
            LaggedStartMap(FadeIn, labels, lag_ratio=0.1),
            run_time=1
        )
        
        bar_animations = []
        for i, (bar, val, val_label) in enumerate(zip(bars, values, value_labels)):
            target_height = val * 0.04
            bar_animations.append(
                AnimationGroup(
                    bar.animate.set_height(target_height).shift(UP * target_height/2),
                    FadeIn(val_label, shift=UP),
                    lag_ratio=0.5
                )
            )
        
        self.play(
            LaggedStart(*bar_animations, lag_ratio=0.2),
            run_time=3
        )
        
        self.stats_elements = VGroup(stats_title, bars, labels, value_labels)
        self.wait(0.5)
    
    def show_defense_measures(self):
        """Show security response and defense measures"""
        # Security team response
        shield = RegularPolygon(n=8, radius=0.8, color=GREEN, fill_opacity=0.3)
        shield_symbol = Text("SEC", font="Arial Bold", font_size=24, color=WHITE)
        security_team = VGroup(shield, shield_symbol).to_edge(RIGHT, buff=1)
        
        self.play(
            DrawBorderThenFill(shield),
            Write(shield_symbol),
            run_time=1
        )
        
        # Security measures deployment
        security_waves = VGroup()
        for i in range(4):
            wave = Arc(
                radius=0.8 + i * 0.5,
                start_angle=PI,
                angle=PI,
                color=GREEN,
                stroke_width=3,
                stroke_opacity=0.7 - i * 0.15
            )
            wave.move_to(security_team.get_center())
            security_waves.add(wave)
        
        self.play(
            LaggedStartMap(Create, security_waves, lag_ratio=0.2),
            run_time=2
        )
        
        # Neutralize attack
        self.play(
            self.github_elements[0].animate.set_color(GREEN),
            self.attack_elements.animate.set_opacity(0.3),
            run_time=1.5
        )
        
        self.security_elements = VGroup(security_team, security_waves)
        self.wait(0.5)
    
    def conclusion_sequence(self):
        """Final message and cleanup"""
        # Security message
        conclusion = VGroup(
            Text("THREAT NEUTRALIZED", font="Arial Bold", font_size=36, color=GREEN),
            Text("Security measures active", font="Arial", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(
            Write(conclusion[0]),
            FadeIn(conclusion[1], shift=UP),
            run_time=1.5
        )
        
        # Pulse effect on conclusion
        self.play(
            conclusion[0].animate.scale(1.2).set_stroke(GREEN, 3),
            run_time=0.5,
            rate_func=there_and_back
        )
        
        self.wait(1)
        
        # Final fadeout
        all_elements = VGroup(
            self.github_elements,
            self.attack_elements,
            self.stats_elements,
            self.security_elements,
            conclusion
        )
        
        self.play(
            FadeOut(all_elements, shift=DOWN),
            run_time=2
        )
        
        # End with logo
        final_logo = Text("GITHUB", font="Arial Bold", font_size=48, color=WHITE)
        final_logo.set_color_by_gradient(BLUE, GREEN)
        
        self.play(
            FadeIn(final_logo, scale=0.5),
            run_time=1
        )
        
        self.play(
            final_logo.animate.scale(1.1),
            run_time=0.5,
            rate_func=there_and_back
        )
        
        self.wait(1)
        
        self.play(FadeOut(final_logo), run_time=1)
        self.wait(0.5)