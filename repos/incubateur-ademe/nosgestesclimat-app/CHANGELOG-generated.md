## Changelog : nosgestesclimat-app (30 derniers jours, au 04 septembre 2026)

### Résumé
Ce mois-ci, l'application a franchi des étapes importantes avec l'ajout de nouvelles fonctionnalités comme la confirmation par email et un catalogue d'actions publiques. L'expérience utilisateur a été enrichie par plusieurs tests A/B et des améliorations d'interface, tandis que des optimisations techniques majeures ont été réalisées pour améliorer la rapidité de navigation (mise en cache, PPR) et la stabilité globale de l'infrastructure.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : 
    - Mise en place de la confirmation par email [#1929].
    - Création d'un catalogue d'actions publiques [#2003].
    - Implémentation de la logique de calcul des données d'événements [#1922].
- **Expérimentations (A/B tests)** : 
    - Tests sur l'affichage des cartes d'actions [#2006], la vente croisée d'actions [#2010] et la mise en page des actions à fort impact [#1997].
- **Améliorations de l'interface et de l'expérience utilisateur** : 
    - Amélioration de la page de détails des actions [#2018] et ajout de descriptions courtes pour les actions [#2012].
    - Ajout d'une section explicative sur les résultats de tests collectifs [#1969].
    - Corrections de styles visuels (inputs, labels, CSS) [#1992, #1995] et de messages d'avertissement [#2004].
- **Corrections** : 
    - Résolution d'un problème de connexion lié aux sessions [#2047].
    - Maintien des paramètres de recherche lors de la navigation entre les étapes [#2027].
    - Correction d'une coquille sur le compteur de la landing page [#2029].
    - Correction de bugs sur la simulation dans les groupes d'amis et la visibilité des actions [#1999, #2002, #1987].

### Évolutions techniques
- **Performance et Architecture** : 
    - Optimisation de la page d'accueil via le PPR (Partial Prerendering) [#2041].
    - Réduction des allers-retours serveur lors des changements de paramètres de simulation [#2035].
    - Optimisation des transactions de base de données pour éviter les blocages [#2036].
    - Augmentation de la mémoire des workers pour prévenir les plantages (OOM) [#2046].
- **Infrastructure et Déploiement** : 
    - Optimisation et extension du cache Nginx (pages publiques, fichiers statiques, exclusion des pages anglaises) [#1953, #2040, #2039].
    - Amélioration de la résilience de Nginx (DNS, retry systemd) [#1966, #2021].
    - Corrections liées au déploiement, à la configuration Nginx et à la CI [#2054, #2033, #1991, #2021].
- **Sécurité et Données** : 
    - Séparation des cookies entre les environnements de production et de préproduction [#2030].
    - Renforcement de la sécurité des sessions et de l'intégrité des liens utilisateurs [#2016, #1973].
    - Nettoyage et migration de la base de données (suppression de tables et de logiques obsolètes, gestion des doublons) [#2032, #2031, #2017, #2015, #1989].
- **Tests** : 
    - Amélioration de la robustesse et de la stabilité des tests de bout en bout (E2E) [#1993, #1990, #1981].

### Autres changements
- **Nettoyage** : Suppression d'un avertissement lors de la phase de build [#2008].
