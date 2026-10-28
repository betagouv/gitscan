## Changelog : anssi-portail (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois a été marqué par un enrichissement significatif des outils d'accompagnement, notamment avec le déploiement d'un simulateur de hameçonnage et de nouveaux modèles de documents dans la boîte à outils. Le portail améliore également sa visibilité et son engagement grâce à l'intégration d'un nouveau blog et d'un parcours de sécurisation plus présent dans l'interface. Parallèlement, une importante phase de restructuration technique a permis de rendre le code plus modulaire et robuste.

### Évolutions fonctionnelles
- **Nouveaux outils de sensibilisation :**
  - Mise en place d'un test de hameçonnage complet incluant une boîte mail simulée, des illustrations animées et des fonctionnalités de vote (adaptées desktop et mobile).
  - Intégration de nouveaux modèles dans la boîte à outils (revue des droits d'accès, revue de comptes utilisateurs, modification de mots de passe et listes d'activités).
- **Parcours de sécurisation :**
  - Meilleure visibilité du parcours de sécurisation via son intégration dans le menu, le pied de page, le héros de la page d'accueil et les résultats des tests (maturité, réflexes cyber).
- **Contenu et Blog :**
  - Lancement d'une section blog permettant la consultation d'articles, la lecture de résumés et la soumission de retours utilisateurs.
- **Annuaire et Contacts :**
  - Enrichissement des données de contact (nationaux, régionaux et sectoriels) et amélioration de la recherche et de l'affichage des cartes de contacts.
- **Expérience utilisateur (UX) :**
  - Optimisation de l'affichage sur tablettes et mobiles pour les tests et les outils.
  - Amélioration de la navigation et correction de divers éléments d'interface (filtres, accordéons, popovers).
  - Mise en place d'un système de retours utilisateurs sur les outils pour améliorer la qualité des services.

### Évolutions techniques
- **Architecture et Refactoring :**
  - Modularisation importante du code : découpage des tests en composants, isolation de la logique de manipulation de fichiers Excel (XLSX) et réorganisation des routes API (outils, annuaires, mini-tests).
  - Refonte de la gestion des utilisateurs et des dossiers pour une meilleure maintenabilité.
  - Implémentation d'un pattern "stratégie" pour certains services.
- **Design System et UI :**
  - Centralisation de la définition de l'UI-KIT et mise à jour vers la version 1.64.0.
  - Intégration native des composants Svelte du DSFR (alertes, notices).
- **Infrastructure et CI/CD :**
  - Migration de la stack vers Node.js 26.
  - Mise à jour de l'environnement Ruby et des runners GitHub Actions.
  - Utilisation de `.nvmrc` comme référence pour la version de Node.js.
- **Qualité et Tests :**
  - Renforcement du typage TypeScript et nettoyage des règles de linting.
  - Amélioration de la structure des tests et remplacement de certains outils de simulation par Vitest.

### Autres changements
- **SEO et Référencement :** Mise à jour des titres, descriptions et métadonnées pour les réseaux sociaux et le sitemap.
- **Nettoyage :** Suppression de nombreuses dépendances et configurations obsolètes (overrides, anciens services Crisp, contacts Jekyll).
- **Documentation :** Mise à jour des contenus textuels et harmonisation de la terminologie.
