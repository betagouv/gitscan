## Changelog : a-just (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la couverture des tests automatisés (E2E), notamment pour le cockpit et le panorama. Des corrections et des améliorations ont également été apportées à la gestion des absences (ASA/EPT) et au simulateur, ainsi que des corrections de sécurité et des ajustements d'interface utilisateur.

### Évolutions fonctionnelles
- Amélioration de la gestion des absences et des indisponibilités, avec migration des règles ASA et intégration dans le cockpit. [#557](https://github.com/betagouv/a-just/pull/557)
- Ajout de tooltips informatifs au calculateur EPT.
- Correction de l'affichage des agents dans les colonnes "Arrivées" et "Départs" du module "Changement dans les effectifs".
- Ajout de tests E2E pour le panorama, notamment pour la vérification des données à compléter. [#556](https://github.com/betagouv/a-just/pull/556)
- Amélioration du calcul du simulateur et correction de l'URL de retour.
- Ajout d'indicateurs d'erreur dans les graphiques du cockpit.
- Correction de l'affichage des contentieux dans les filtres.

### Évolutions techniques
- Mise à jour des dépendances `@emnapi` et suppression des entrées obsolètes `esbuild`.
- Correction de l'accès aux variables d'environnement dans l'API de connexion.
- Amélioration de la méthode de récupération de l'URL du serveur dans les tests E2E.
- Mise à jour de la configuration de Cypress pour une meilleure compatibilité et résolution de problèmes.
- Correction de la validation des URLs des iframes pour renforcer la sécurité.
- Refactorisation du code pour supprimer les duplications.
- Passage à Cypress 15 et adaptation des tests.

### Autres changements
- Ajout de fichiers `.env.example` pour les tests E2E.
- Ajout de logs pour faciliter le débogage et le suivi des événements.
- Amélioration de la gestion des erreurs et des messages d'alerte dans le cockpit.
- Corrections mineures de grammaire et de typographie dans les logs.
- Mise à jour de la version du projet.
- Ajout de règles ASA.
- Correction d'un bug lié à la date de début des indisponibilités.
- Amélioration de la gestion des erreurs dans les graphiques du cockpit.
- Ajout de tests E2E pour la validation des données disponibles dans le panorama.
