## Changelog : seves (30 derniers jours, au 08/10/2026)

### Résumé
Cette période a été marquée par un développement intensif du module Santé Animale (SA), avec l'introduction de nouvelles fonctionnalités de synthèse, de meilleurs outils de recherche et une gestion plus complète du cycle de vie des événements. L'expérience utilisateur a été fluidifiée par une interface plus intuitive (notamment via l'utilisation de sélecteurs enrichis) et l'ajout d'une page d'accueil publique pour la plateforme.

### Évolutions fonctionnelles

**Santé Animale (SA)**
- **Nouvelles fonctionnalités de gestion** : Ajout d'un bloc "Enquête épidémiologique", possibilité de clôturer un événement et ajout d'une fonction de synthèse pour les événements SA.
- **Amélioration de la saisie** : Optimisation des formulaires de création (meilleure gestion des espèces concernées, des localisations et des contacts) et ajout de la possibilité de créer un événement depuis n'importe quelle page SA.
- **Recherche et visualisation** : Ajout de filtres de recherche avancés dans la liste des événements SA et mise à jour de l'affichage des listes pour plus de clarté.
- **Export et documents** : Possibilité d'exporter les événements SA au format Word (.docx).

**Interface et Expérience Utilisateur (UI/UX)**
- **Navigation** : Mise en ligne d'une page d'accueil publique pour SEVES.
- **Saisie simplifiée** : Généralisation de l'utilisation de composants "TreeSelect" pour faciliter la sélection de maladies ou d'espèces dans les formulaires et les modales.
- **Aide et guidage** : Ajout de modales d'aide, de liens vers la documentation et de textes d'explication pour accompagner l'utilisateur dans les formulaires complexes.
- **Adaptabilité** : Amélioration de l'affichage sur petits écrans et ajustement des composants visuels (modales, colonnes de formulaires).

**Autres modules**
- **TIAC / Alimentation** : Renommage de "SSA" en "Alim" pour plus de cohérence et corrections sur la gestion des menus et des notifications.
- **Référentiels** : Mise à jour des listes d'organismes (ajout de nouveaux insectes) et des laboratoires de référence.

### Évolutions techniques

**Sécurité et Infrastructure**
- **Protection** : Mise en place d'un Web Application Firewall (WAF).
- **Configuration réseau** : Ajustement de la configuration Caddy pour la gestion des plages privées et mise à jour des politiques CSP pour permettre les téléchargements via Metabase.

**Performance et Qualité du code**
- **Optimisation** : Amélioration des performances de la page de création d'événements SA.
- **Maintenance du code** : Nettoyage important du code via l'outil Ruff et refactorisation de la gestion des sous-documents.
- **Gestion des dépendances** : Mise à jour de plusieurs composants internes et de l'environnement Go.

**Tests et CI/CD**
- **Fiabilité des tests** : Correction de tests "instables" (flaky tests) concernant l'historique TIAC et la synthèse SA.
- **Amélioration de la suite de tests** : Optimisation des usines de données (factories) pour les tests SA et amélioration des tests ADIS.

### Autres changements
- **Documentation** : Mise à jour des textes d'aide et des notices informatives.
- **Base de données** : Correction de migrations sur la branche principale.
