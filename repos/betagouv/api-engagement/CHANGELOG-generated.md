## Changelog : api-engagement (30 derniers jours, au 20/10/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans l'amélioration de l'expérience de matching et de l'engagement des utilisateurs. Les évolutions se concentrent sur une meilleure visibilité des missions (nouvelles pages dédiées, statistiques publiques), une navigation mobile optimisée et un moteur de recherche plus performant. Parallèlement, des efforts significatifs ont été portés sur la précision de l'analyse de données et l'optimisation technique de l'API.

### Évolutions fonctionnelles
- **Expérience de recherche et matching** :
    - Amélioration du classement des missions via un catalogue de matching précalculé [#1604](https://github.com/betagouv/api-engagement/issues/1604).
    - Introduction de nouveaux filtres par activités de mission [#1595](https://github.com/betagouv/api-engagement/issues/1595).
    - Optimisation de l'affichage mobile avec un panneau de résultats coulissant (bottom sheet) [#1607](https://github.com/betagouv/api-engagement/issues/1607) et des filtres persistants sur la page des missions [#1606](https://github.com/betagouv/api-engagement/issues/1606).
- **Nouveaux contenus et pages** :
    - Création de nouvelles pages d'atterrissage (landing pages) pour "Engagement Sécurité" [#1601](https://github.com/betagouv/api-engagement/issues/1601) et "Chacun pour tous" [#1548](https://github.com/betagouv/api-engagement/issues/1548).
    - Mise en ligne d'une page de statistiques publiques basée sur des tableaux de bord Metabase [#1526](https://github.com/betagouv/api-engagement/issues/1526).
    - Refonte visuelle de la page d'accueil [#1484](https://github.com/betagouv/api-engagement/issues/1484).
- **Parcours utilisateur et engagement** :
    - Refonte du quiz incluant une étape de collecte d'emails pour améliorer la conversion [#1553](https://github.com/betagouv/api-engagement/issues/1553).
    - Ajout de prévisualisations de partage social et optimisation des balises SEO pour une meilleure visibilité [#1530](https://github.com/betagouv/api-engagement/issues/1530).
- **Outils d'administration et de diffusion** :
    - Possibilité pour les administrateurs de modifier une mission directement depuis sa page de détail [#1560](https://github.com/betagouv/api-engagement/issues/1560).
    - Enrichissement des données pour les diffuseurs (informations sur les candidatures attendues) [#1598](https://github.com/betagouv/api-engagement/issues/1598).

### Évolutions techniques
- **Optimisation des performances** :
    - Mise en place de la compression des réponses API [#1538](https://github.com/betagouv/api-engagement/issues/1538).
    - Implémentation de la pagination par curseur pour la liste des missions (v2) [#1486](https://github.com/betagouv/api-engagement/issues/1486).
    - Mise en cache des cartes Metabase publiques via un service de cache partagé [#1527](https://github.com/betagouv/api-engagement/issues/1527).
- **Moteur de matching et API** :
    - Refonte de l'algorithme du moteur de matching [#1500](https://github.com/betagouv/api-engagement/issues/1500).
    - Amélioration de la rapidité du matching par le pré-filtrage des candidats par localisation [#1597](https://github.com/betagouv/api-engagement/issues/1597).
    - Amélioration de la précision de la géolocalisation pour réduire les erreurs d'adresses non trouvées [#1510](https://github.com/betagouv/api-engagement/issues/1510).
- **Observabilité et Analytics** :
    - Renforcement du suivi analytique (événements de tracking, réponses aux quiz, étapes du tunnel de conversion) [#1594](https://github.com/betagouv/api-engagement/issues/1594).
    - Amélioration de la remontée des erreurs vers Sentry pour un diagnostic plus précis [#1554](https://github.com/betagouv/api-engagement/issues/1554).
- **Infrastructure** :
    - Augmentation de l'espace disque alloué à Typesense [#1456](https://github.com/betagouv/api-engagement/issues/1456).

### Autres changements
- **SEO et Conformité** :
    - Mise en place du fichier `robots.txt`, du `sitemap.xml` et gestion des balises `noindex` pour les pages sensibles [#1509](https://github.com/betagouv/api-engagement/issues/1509).
    - Mise en conformité de la politique de confidentialité avec les outils de collecte de données (PostHog, Brevo) [#1591](https://github.com/betagouv/api-engagement/issues/1591).
- **Accessibilité** :
    - Corrections liées à l'audit RGAA sur le tableau de bord [#1504](https://github.com/betagouv/api-engagement/issues/1504).
