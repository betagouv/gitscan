## Changelog : espace-membre-next (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité, la correction de bugs et l'optimisation de certaines fonctionnalités existantes.  Une nouvelle fonctionnalité de recherche de startups a été ajoutée, et des améliorations ont été apportées à la gestion des phases et des emails. Des nettoyages de code et des suppressions de fonctionnalités obsolètes ont également été effectués.

### Évolutions fonctionnelles
- **Recherche de startups :** Ajout d'une fonctionnalité de recherche avec un champ de sélection pour les startups [#1324](https://github.com/betagouv/espace-membre-next/issues/1324).
- **Gestion des phases :** Amélioration de la gestion des phases [#1304](https://github.com/betagouv/espace-membre-next/issues/1304).
- **Création d'emails :** Correction d'un bug empêchant la création d'emails lorsque l'adresse email principale n'était pas définie [#1342](https://github.com/betagouv/espace-membre-next/issues/1342).
- **Onboarding :**  Les attributaires ne se voient plus créer d'email lors de l'onboarding [#1305](https://github.com/betagouv/espace-membre-next/issues/1305).

### Évolutions techniques
- **Accessibilité (RGAA) :**
    - Ajout de l'attribut `lang` sur la balise `<html>` pour améliorer l'accessibilité [#1361](https://github.com/betagouv/espace-membre-next/issues/1361).
    - Remplacement de labels orphelins par des éléments de label stylisés pour une meilleure accessibilité [#1363](https://github.com/betagouv/espace-membre-next/issues/1363).
    - Amélioration de l'accessibilité des éléments `onClick` statiques pour les rendre utilisables au clavier [#1364](https://github.com/betagouv/espace-membre-next/issues/1364).
    - Fin de la mise en place des règles jsx-a11y pour la conformité RGAA [#1365](https://github.com/betagouv/espace-membre-next/issues/1365).
- **Sécurité :**
    - Renforcement de la vérification d'authentification lors de la mise à jour des événements [#1357](https://github.com/betagouv/espace-membre-next/issues/1357).
    - Suppression de TODO liés à l'authentification obsolètes [#1354](https://github.com/betagouv/espace-membre-next/issues/1354).
- **Migration MJML :** Migration du système d'email vers MJML [#1350](https://github.com/betagouv/espace-membre-next/issues/1350).
- **Composant DSFR :** Utilisation du composant `DataVisualization` de DSFR au lieu d'un asset SVG supprimé [#1351](https://github.com/betagouv/espace-membre-next/issues/1351).
- **Optimisation du routage :** Simplification du routage et utilisation accrue du rendu côté serveur (SSR) [#1326](https://github.com/betagouv/espace-membre-next/issues/1326).
- **Timeout dimail-sync :** Augmentation du timeout pour la synchronisation des emails [#1372](https://github.com/betagouv/espace-membre-next/issues/1372).

### Autres changements
- **Nettoyage de code :** Suppression de code obsolète lié à Mattermost [#1325](https://github.com/betagouv/espace-membre-next/issues/1325) et à l'ancien système de suppression de comptes Matomo/Sentry [#1322](https://github.com/betagouv/espace-membre-next/issues/1322).
- **Configuration :** Suppression de variables d'environnement inutiles [#1329](https://github.com/betagouv/espace-membre-next/issues/1329) et du fichier `.dotenv` [#1339](https://github.com/betagouv/espace-membre-next/issues/1339).
- **Refactoring :** Renommage et documentation de la tâche `phase-reminder` [#1374](https://github.com/betagouv/espace-membre-next/issues/1374).
- **Mises à jour :** Quelques mises à jour de dépendances [#1331](https://github.com/betagouv/espace-membre-next/issues/1331).
- **Cleanup:** Nettoyage de code lié aux anciens emails [#1375](https://github.com/betagouv/espace-membre-next/issues/1375).
