## Changelog : mon-indemnisation-justice (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives concernant la gestion des dossiers, l'import de données, l'expérience utilisateur pour les agents et l'implémentation du test d'éligibilité dans l'espace public. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Test d'éligibilité:** Implémentation du test d'éligibilité dans l'espace public, incluant la création des étapes et l'utilisation de formulaires Tanstack. [#33aa28c](https://github.com/betagouv/mon-indemnisation-justice/commit/33aa28c)
- **Gestion des agents:**
    - Création d'un onglet "Agents à valider" pour faciliter la gestion des nouveaux agents.
    - Restriction de l'accès à certaines fonctionnalités pour les agents MJ sans rôle AGENT_DOSSIER.
    - Amélioration de l'affichage des listes d'agents (actifs/inactifs).
- **Pièces jointes:** Ajout d'une modale de suppression de pièces jointes (fonctionnalité non encore active). [#1d377d4](https://github.com/betagouv/mon-indemnisation-justice/commit/1d377d4)
- **Bailleurs sociaux:** Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours utilisateur associé. [#1d20fa9](https://github.com/betagouv/mon-indemnisation-justice/commit/1d20fa9)
- **Recherche:** Possibilité de modifier les critères de recherche. [#b3785de](https://github.com/betagouv/mon-indemnisation-justice/commit/b3785de)
- **Gestion des erreurs:** Amélioration de la gestion et de l'affichage des erreurs FIP6 et FDO. [#8272609](https://github.com/betagouv/mon-indemnisation-justice/commit/8272609), [#4d0b818](https://github.com/betagouv/mon-indemnisation-justice/commit/4d0b818)

### Évolutions techniques
- **Worker:**
    - Refonte de l'architecture du worker pour utiliser `pierrelemee/supervisor-docker` pour la gestion et la surveillance des tâches cron. [#dd74ef7](https://github.com/betagouv/mon-indemnisation-justice/commit/dd74ef7)
    - Déploiement des applications web et worker sur l'environnement `develop`. [#dad9add](https://github.com/betagouv/mon-indemnisation-justice/commit/dad9add)
    - Création d'une image Docker pour l'exécution des tâches cron. [#a0e9e80](https://github.com/betagouv/mon-indemnisation-justice/commit/a0e9e80)
- **Import de données:** Création d'un importeur CSV basique et importation des données des gendarmeries. [#ed7b87b](https://github.com/betagouv/mon-indemnisation-justice/commit/ed7b87b), [#8a87013](https://github.com/betagouv/mon-indemnisation-justice/commit/8a87013)
- **Frontend:**
    - Ajout de `vite-plugin-node-polyfills` pour résoudre les erreurs de conversion node vers browser. [#7de58ac](https://github.com/betagouv/mon-indemnisation-justice/commit/7de58ac)
    - Fluidification de l'affichage des champs en tiroir et possibilité de masquer les outils Tanstack. [#e8aeaf1](https://github.com/betagouv/mon-indemnisation-justice/commit/e8aeaf1)
- **Authentification:** Injection de l'URL de déconnexion dans le contexte agent et correction de l'URL de déconnexion pour ProConnect. [#78a286f](https://github.com/betagouv/mon-indemnisation-justice/commit/78a286f), [#66e71ef](https://github.com/betagouv/mon-indemnisation-justice/commit/66e71ef), [#2da6288](https://github.com/betagouv/mon-indemnisation-justice/commit/2da6288)

### Autres changements
- **Documentation:** Intégration de la FAQ modifiée (en cours). [#c7a45be](https://github.com/betagouv/mon-indemnisation-justice/commit/c7a45be)
- **Tests:** Ajout de tests unitaires pour la route de suppression et corrections de tests existants. [#47ad9ec](https://github.com/betagouv/mon-indemnisation-justice/commit/47ad9ec), [#7062ac8](https://github.com/betagouv/mon-indemnisation-justice/commit/7062ac8)
- **Corrections:**
    - Correction d'un bug empêchant le fonctionnement de la modale de mot de passe oublié. [#f120742](https://github.com/betagouv/mon-indemnisation-justice/commit/f120742)
    - Correction pour gérer le cas où l'adresse est manquante sur un dossier. [#60bcdf2](https://github.com/betagouv/mon-indemnisation-justice/commit/60bcdf2)
    - Correction pour le support de `react-pdf` sur Safari iOS. [#c83cf05](https://github.com/betagouv/mon-indemnisation-justice/commit/c83cf05)
    - Correction d'un problème avec `vite-plugin-static-copy` en dépendance de développement. [#a871324](https://github.com/betagouv/mon-indemnisation-justice/commit/a871324)
- **Email:** Envoi d'emails au chargement des fixtures et des déclarations FDO. [#f66b0e8](https://github.com/betagouv/mon-indemnisation-justice/commit/f66b0e8), [#1927e25](https://github.com/betagouv/mon-indemnisation-justice/commit/1927e25)
- **Frise temporelle:** Création du composant Frise temporelle pour afficher l'historique avec des badges de couleur. [#e909378](https://github.com/betagouv/mon-indemnisation-justice/commit/e909378)
