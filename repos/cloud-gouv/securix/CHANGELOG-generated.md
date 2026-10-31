## Changelog : securix (30 derniers jours, au 29 octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience de navigation web, le renforcement de la fiabilité des outils de sécurité (Yubikey, IPsec) et l'introduction d'un système de télémétrie de base pour la communauté. La stabilité du système a également été renforcée via des corrections sur les mises à jour automatiques et la gestion des noms d'hôte.

### Évolutions fonctionnelles
- **Navigation Web** : 
    - Firefox est désormais maintenu par défaut dans les modules d'outils.
    - Améliorations de Chromium, incluant la gestion de l'économie d'énergie [#312] et l'obligation de l'utilisation de scripts PAC en mode PAC.
- **Sécurité et outils** : 
    - Amélioration de l'outil de réinitialisation des clés Yubikey [#302].
- **Télémétrie** : Mise en place d'un système de rapport de télémétrie de base pour la communauté, incluant le nom d'hôte et le temps de démarrage.

### Évolutions techniques
- **Réseau et connectivité** : Amélioration de la correspondance des noms de domaine (DN) pour les profils IPsec, indépendamment de leur ordre [#279].
- **Système et stabilité** :
    - Correction du mécanisme de repli (fallback) du nom d'hôte pour les machines non identifiées [#266].
    - Résolution d'un problème de temporisation (dead timer) affectant les mises à jour automatiques [#277].
    - Ajout d'une option d'activation pour les variantes de l'interface graphique [#311].
- **Infrastructure et CI/CD** :
    - Renforcement de la sécurité des GitHub Actions en appliquant des permissions vides par défaut [#306].
    - Amélioration et couverture de test de l'installateur netboot.
- **Correctifs divers** : Correction de la génération d'inventaire [#303] et optimisation de la gestion des commandes `sudo` dans certains scripts [#284].

### Autres changements
- **Documentation** : Corrections typographiques et de mise en forme dans le README [#297].
- **Maintenance** : 
    - Mise à jour de la gestion des propriétaires du code (Code Owners) [#305].
    - Uniformisation des en-têtes de licence SPDX [#308].
