## Changelog : csplab (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'interface utilisateur (ATS), l'enrichissement des fonctionnalités d'ingestion de données (notamment pour Talentsoft), la mise en place d'une authentification plus robuste et l'amélioration de l'infrastructure et des outils de développement. Des bases solides sont posées pour les prochaines étapes du projet, notamment en matière de gestion des utilisateurs et de sécurité.

### Évolutions fonctionnelles

*   **ATS (Application de Suivi des Candidatures) :**
    *   Ajout de composants d'interface utilisateur de base : icônes, boutons, badges, conteneurs de contenu, barres de pagination et tableaux. [#812](https://github.com/betagouv/csplab/issues/812)
    *   Implémentation d'une barre latérale pour la navigation. [#846](https://github.com/betagouv/csplab/issues/846)
    *   Ajout d'un composant de fil d'Ariane (breadcrumb). [#852](https://github.com/betagouv/csplab/issues/852)
    *   Possibilité d'activer des actions sur les lignes ou cellules d'un tableau. [#860](https://github.com/betagouv/csplab/issues/860)
    *   Mise en place d'un en-tête de page générique. [#853](https://github.com/betagouv/csplab/issues/853)
    *   Première implémentation de la page "Mes recrutements". [#838](https://github.com/betagouv/csplab/issues/838)
*   **Gestion des Recruteurs :**
    *   Interface pour visualiser les détails d'un recrutement. [#856](https://github.com/betagouv/csplab/issues/856)
    *   Interface pour mettre à jour les étapes de recrutement d'un organisme. [#835](https://github.com/betagouv/csplab/issues/835)
    *   Initialisation des étapes de recrutement. [#819](https://github.com/betagouv/csplab/issues/819)
*   **Ingestion de données :**
    *   Importation de toutes les offres Talentsoft via des webhooks CREE. [#858](https://github.com/betagouv/csplab/issues/858)
    *   Possibilité de rendre les champs client/url optionnels pour les sources API. [#854](https://github.com/betagouv/csplab/issues/854)
    *   Ajout d'un endpoint pour récupérer les sources par UUID. [#825](https://github.com/betagouv/csplab/issues/825)
*   **Authentification :**
    *   Implémentation de l'authentification par email et mot de passe. [#750](https://github.com/betagouv/csplab/issues/750)
    *   Ajout de l'authentification à deux facteurs (2FA) sur l'interface d'administration Django. [#699](https://github.com/betagouv/csplab/issues/699)

### Évolutions techniques

*   **Infrastructure & CI/CD :**
    *   Mise en place de releases Sentry lors des déploiements pour web, OCR et ingestion. [#850](https://github.com/betagouv/csplab/issues/850)
    *   Amélioration de la configuration de déploiement de Storybook. [#872](https://github.com/betagouv/csplab/issues/872) et [#871](https://github.com/betagouv/csplab/issues/871)
    *   Ajout de workflows pour les previews de branches Storybook à la demande. [#867](https://github.com/betagouv/csplab/issues/867)
    *   Correction de problèmes de boucle d'import Celery et simplification de la configuration. [#862](https://github.com/betagouv/csplab/issues/862)
    *   Amélioration de la gestion des logs et ajout de logs d'API. [#720](https://github.com/betagouv/csplab/issues/720) et [#733](https://github.com/betagouv/csplab/issues/733)
    *   Ajout d'un script pour mettre à jour les dépendances. [#832](https://github.com/betagouv/csplab/issues/832)
    *   Mise en place d'un script de sauvegarde de la base de données sur Scaleway. [#833](https://github.com/betagouv/csplab/issues/833)
*   **Architecture & Code :**
    *   Refactoring de l'architecture pour séparer les couches domaine et présentation. [#863](https://github.com/betagouv/csplab/issues/863)
    *   Déplacement du modèle `Source` dans une librairie partagée. [#847](https://github.com/betagouv/csplab/issues/847)
    *   Simplification de l'interface des événements de domaine. [#811](https://github.com/betagouv/csplab/issues/811)
    *   Utilisation de décorateurs `patch` pour améliorer la lisibilité des tests. [#849](https://github.com/betagouv/csplab/issues/849)
    *   Amélioration de la gestion des erreurs Celery avec la capture des exceptions dans Sentry. [#861](https://github.com/betagouv/csplab/issues/861)
    *   Passage à un modèle utilisateur personnalisé Django. [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616) et [#632](https://github.com/betagouv/csplab/issues/632)

### Autres changements

*   Ajout de seed de données de recruteur pour les tests. [#859](https://github.com/betagouv/csplab/issues/859)
*   Documentation de l'API pour les utilisateurs non techniques. [#813](https://github.com/betagouv/csplab/issues/813)
*   Ajout d'une page pour afficher la documentation de l'API. [#820](https://github.com/betagouv/csplab/issues/820)
*   Mise à jour des dépendances de plusieurs modules (web, notebook, ocr, ingestion).
*   Correction de divers bugs et améliorations de la qualité du code.
*   Ajout d'un fichier `security.txt` pour la divulgation responsable des vulnérabilités. [#695](https://github.com/betagouv/csplab/issues/695)
*   Amélioration des tests et de la couverture de code.
*   Mise à jour du fichier CHANGELOG.md pour les versions précédentes. [#648](https://github.com/betagouv/csplab/issues/648) et [#567](https://github.com/betagouv/csplab/issues/567)
