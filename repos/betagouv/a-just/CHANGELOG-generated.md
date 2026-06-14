## Changelog : a-just (30 derniers jours, au 12 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur, notamment sur les pages Cockpit et Panorama, avec l'ajout de tests E2E pour garantir la stabilité et la fiabilité des nouvelles fonctionnalités. Des corrections ont également été apportées pour améliorer la gestion des dates, des absences et des données des agents. Des mises à jour de l'infrastructure et des dépendances ont été effectuées pour assurer la performance et la sécurité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des données sur la page Panorama : ajout de tooltips, d'un bouton "Qu'est-ce que c'est ?" pour le ventilateur des ressources humaines, et mise à jour de l'aide pas à pas (IntroJS).
- Amélioration de la page Cockpit : ajout de tooltips pour le calculateur, affichage des entrées et sorties, et correction de l'affichage des dates.
- Correction de l'affichage des agents dans la colonne "Arrivées" et "Départs" de "Changement dans les effectifs".
- Correction de l'affichage des contentieux après la complétion des données.
- Amélioration de la gestion des dates de début pour les simulations.
- Correction de la migration des décharges syndicales.
- Mise à jour de la catégorisation ASA.
- Correction de l'affichage des contentieux pour lesquels des données doivent être complétées (bleu).
- Ajout de la possibilité de modifier la date de début des simulateurs blancs.

### Évolutions techniques
- Refactorisation des workflows GitHub Actions pour simplifier les déploiements.
- Mise à jour des dépendances, notamment `@emnapi`.
- Amélioration de la configuration de Cypress pour les tests E2E.
- Correction de l'URL pour l'extracteur de données 2026.
- Ajout de délais d'attente dans les tests E2E pour améliorer la stabilité.
- Mise à jour de Redis pour redémarrer automatiquement en cas de problème.
- Ajout de règles ASA pour la gestion des absences.
- Ajout de CSP security.
- Suppression de nightly-sandbox.yml.

### Autres changements
- Correction de fichiers de nomenclature [#564](https://github.com/betagouv/a-just/issues/564).
- Correction de l'extracteur de collecte 2026.
- Ajout de logs pour faciliter le débogage.
- Suppression de code inutilisé.
- Mise à jour de la version de l'application.
- Ajout d'un fichier `.env.example` pour les tests E2E.
- Synchronisation des origines.
- Correction de la gestion de l'état de chargement dans le composant PopinEditActivitiesComponent.
- Correction d'un bug lié à la première date à vérifier dans le futur.
- Ajout d'un rôle pour mettre à jour le panorama.
- Correction d'un bug lié à la gestion des entrées et sorties dans le composant ReferentielCalculatorComponent.
- Correction d'un bug lié à la gestion des dates dans le cockpit.
- Suppression d'une branche sandbox.
- Fusion de branches `dev` et `sandbox`.
- Correction de l'appel de script JS.
- Correction de l'étiquette "contentieux" dans les tests E2E.
- Correction d'un bug lié à la gestion des absences.
- Correction de la duplication d'agents.
- Ajout de tests E2E pour la page Panorama.
- Ajout de tests E2E pour la page Cockpit.
