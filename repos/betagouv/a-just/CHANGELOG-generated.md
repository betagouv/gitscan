## Changelog : a-just (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la couverture des tests automatisés, notamment avec l'ajout de tests E2E pour plusieurs fonctionnalités clés. Des corrections et des améliorations ont été apportées à l'interface utilisateur, notamment au niveau du cockpit et du panorama, ainsi que des ajustements pour la gestion des absences et des données. Des mises à jour de l'infrastructure et des dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Amélioration de la gestion des dates de début dans l'interface utilisateur, notamment pour les situations et les simulations.
- Correction de l'affichage des agents dans les colonnes "Arrivées" et "Départs" des changements d'effectifs.
- Ajout d'un bouton "Qu'est-ce que c'est ?" pour les utilisateurs non autorisés à éditer les ressources humaines dans le ventilateur.
- Amélioration de l'expérience utilisateur avec l'ajout de tooltips pour le calculateur EPT.
- Correction de l'affichage des contentieux après la complétion des données.
- Amélioration de l'affichage des données disponibles dans le panorama.
- Correction de l'affichage des décharges syndicales.
- Mise à jour de la catégorisation ASA.
- Possibilité de modifier les dates de début des simulations blanches.
- Correction de l'affichage des absences.

### Évolutions techniques
- Refactorisation du workflow GitHub Actions pour simplifier les déploiements.
- Mise à jour des dépendances et des fichiers de verrouillage (package-lock, yarn.lock).
- Amélioration de la configuration de Cypress pour les tests E2E.
- Ajout de tests E2E pour le panorama, les données de contentieux et les filtres.
- Correction de la configuration de Redis pour un redémarrage automatique.
- Ajout de mesures de sécurité CSP (Content Security Policy).
- Suppression de fichiers et de configurations inutilisés.
- Migration de l'ASA vers l'absentéisme.
- Correction de l'importation de `normalizeDate` dans les tests E2E.
- Mise à jour de l'extracteur-collecte.

### Autres changements
- Correction de la nomenclature des fichiers [#564](https://github.com/betagouv/a-just/issues/564).
- Ajout de logs pour faciliter le débogage.
- Correction de fautes de frappe dans les logs.
- Mise à jour de la version du projet.
- Ajout d'un fichier `.env.example` pour les tests E2E.
- Amélioration de la documentation et des commentaires.
- Suppression d'un workflow de sandbox nightly.
- Correction de l'URL dans les tests E2E pour l'extracteur d'effectifs.
- Ajout de conditions et d'attentes dans les tests E2E pour améliorer leur fiabilité.
- Correction de l'étiquette "contentieux" dans les tests E2E.
- Mise à jour de l'IntroJS sur la page du cockpit et du panorama.
- Correction d'un script JavaScript.
