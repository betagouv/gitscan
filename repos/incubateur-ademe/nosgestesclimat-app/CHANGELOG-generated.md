## Changelog : nosgestesclimat-app (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience liée aux "Actions" (nouveaux contenus, tests de présentation et déploiement progressif) et par une optimisation majeure des performances de la plateforme. L'application est désormais plus rapide grâce à de nouveaux systèmes de mise en cache et plus stable grâce à un renforcement des tests automatisés.

### Évolutions fonctionnelles
- **Expérience des Actions :**
    - Déploiement progressif de nouvelles actions [#1964] et support de toutes les régions du modèle [#1961].
    - Ajout de descriptions courtes pour les actions [#2012] et réactivation des actions liées aux services sociétaux [#1955].
    - Mise en place de tests A/B sur le design des cartes d'actions [#2006] et sur la mise en page des actions à fort impact [#1997].
    - Introduction de fonctionnalités de "cross-sell" pour suggérer des actions complémentaires [#2010] et création d'un catalogue d'actions publiques [#2003].
    - Refonte des actions pour les groupes d'amis [#1987].
- **Nouvelles fonctionnalités et interface :**
    - Ajout de la confirmation par email [#1929].
    - Ajout d'une section explicative sur la page des résultats de tests collectifs [#1969].
    - Remplacement des notifications d'IA par des "funfacts" pour une approche plus ludique [#1970].
    - Améliorations visuelles (CSS) sur les labels, les suggestions, les champs de saisie et l'affichage des icônes sur desktop [#1995, #1992, #1960].
- **Corrections de bugs :**
    - Résolution de problèmes de réinitialisation de simulation dans les groupes d'amis [#1999].
    - Correction de l'affichage des actions dans le catalogue personnalisé lors de simulations incomplètes [#2002].
    - Correction de liens externes brisés dans les iframes [#1962] et des URLs du tutoriel [#1935].
    - Correction de problèmes liés à l'authentification et à la migration des simulations de connexion [#1959, #1930].

### Évolutions techniques
- **Performance et Infrastructure :**
    - Mise en place d'un système de cache via un reverse proxy Nginx (remplaçant un CDN) avec limitation de débit [#1941].
    - Optimisation de la vitesse d'accès via la mise en cache de la page d'accueil et des tutoriels pour les utilisateurs anonymes [#1946] et le proxying des assets S3 [#1949].
    - Gestion du cache pour la bannière en environnement de préproduction [#1991].
- **Stabilité et Tests :**
    - Amélioration significative de la robustesse et de la fiabilité des tests de bout en bout (E2E) sur la CI et en préproduction [#1993, #1990, #1981, #1977].
- **Architecture et Modèle :**
    - Mises à jour successives du modèle métier [#2000, #1965] et correction de la gestion des versions du modèle [#1972].
    - Refactorisation de la gestion des erreurs d'authentification pour plus de typage et de sécurité [#1942].
    - Migration vers un nouveau système de gestion des composants mis en cache [#1945].
    - Ajout de vues anonymes pour les groupes dans le schéma de base de données [#1989].

### Autres changements
- Refonte du sitemap pour améliorer le référencement [#1944].
- Optimisation du processus de build pour réduire les avertissements de fichiers [#2008].
- Ajout d'un script pour automatiser les mises à jour des versions du modèle [#1980].
