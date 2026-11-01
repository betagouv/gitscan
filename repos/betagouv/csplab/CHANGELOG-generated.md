## Changelog : csplab (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la maturité de ses outils de recrutement et de gestion des candidatures, notamment grâce à l'introduction de fonctionnalités de collaboration (notes, étiquettes, messagerie enrichie). Parallèlement, une refonte structurelle majeure a été entreprise pour aligner le code sur les nouveaux standards de l'équipe, tout en renforçant la fiabilité et la précision de l'importation des offres de postes.

### Évolutions fonctionnelles
- **Gestion des candidatures et messagerie** : 
    - Ajout de notes (privées, modification, suppression et affichage de liste) et intégration de l'historique d'activité dans le panneau de candidature [#2116, #2100, #2098, #1805, #1668].
    - Amélioration de la messagerie avec la possibilité de joindre des fichiers, de répondre directement dans une conversation et gestion du marquage des messages lus/non lus [#1666, #1664, #1973, #1971, #1981].
- **Outils recruteurs** : 
    - Mise en place d'un système complet de gestion d'étiquettes (création, modification de couleur/libellé, statistiques d'utilisation et suppression) [#2094, #2036, #2022, #2065, #2047].
    - Amélioration de l'interface utilisateur : recherche d'organismes insensible aux accents [#2141], alignement du Kanban sur les tableaux [#2114], et nouveau sélecteur d'espace [#2016].
    - Distinction entre notes d'équipe et notes personnelles [#2096].
- **Ingestion de données** : 
    - Enrichissement des données importées depuis Talentsoft (documents requis, contacts, dates de vacance de poste et emails) [#2092, #1936, #1990, #1946].
    - Renforcement de la qualité des données : validation stricte des zones géographiques, des codes pays et des catégories d'offres [#2143, #2148, #2076, #2073, #2069].

### Évolutions techniques
- **Architecture et Refactoring** : 
    - Migration massive des services (recrutement, organismes, identité) vers les nouveaux standards architecturaux (ADR-009 et ADR-011) pour améliorer la maintenabilité [#2017, #1995, #2021, #1923, #1814, #1746, #1713, #1704].
    - Nettoyage du code et suppression de composants obsolètes (dead code) [#1931, #1928, #1796].
- **Sécurité et Identité** : 
    - Renforcement de la gestion des accès et de la sécurité (limitation du débit des requêtes, gestion des sessions et filtrage des organismes supprimés) [#1970, #1966, #1807, #1964, #1762].
    - Limitation des accès par canal d'accès et par endpoint [#1673, #1660].
- **Infrastructure et CI/CD** : 
    - Optimisation des pipelines de CI (réduction du nombre de jobs et annulation des exécutions obsolètes) [#2134, #2136].
    - Mise à jour de l'infrastructure : passage à PostgreSQL 18 et utilisation du réseau privé Scaleway pour les échanges entre services [#1987, #1974].
- **API** : 
    - Francisation de nombreux champs et filtres de l'API d'ingestion [#1852, #1847, #2051].
    - Amélioration des performances et de l'expérience développeur via la pagination DRF et le support du format Markdown pour les descriptions [#2067, #2008].

### Autres changements
- **Documentation** : 
    - Amélioration de la documentation de l'API avec l'ajout de pages d'aide, de contact et de changelogs [#1932, #1920, #1727].
    - Documentation des correspondances de champs pour l'ingestion de données [#1804, #1789, #2034].
