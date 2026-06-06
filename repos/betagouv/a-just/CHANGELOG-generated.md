## Changelog : a-just (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la fiabilité de l'application, notamment au niveau des tests automatisés et de la sécurité. Des corrections ont été apportées à l'affichage des données dans le cockpit et le panorama, ainsi que des ajustements pour améliorer l'expérience utilisateur, en particulier pour les simulations et les alertes.

### Évolutions fonctionnelles
- Amélioration des tests E2E (End-to-End) pour la page Panorama, incluant la vérification de l'affichage des données à compléter et des agents nouvellement ajoutés dans les effectifs. [#557](https://github.com/betagouv/a-just/pull/557)
- Ajout de tests E2E pour les dernières données disponibles dans le Panorama.
- Correction de l'affichage des contentieux dans le cockpit.
- Amélioration de l'interface utilisateur du "Ventilateur Human Ressource" en masquant un bouton "Qu'est ce que c'est ?" pour les utilisateurs sans permission d'édition.
- Correction de l'affichage des dates de début dans le simulateur.
- Correction de l'affichage des agents dans les colonnes "Arrivées" et "Départs" du "Changement dans les effectifs".
- Correction de l'affichage des données de décharge syndicale.
- Ajout d'info-bulles (tooltips) pour faciliter la compréhension des données dans le cockpit et le panorama.
- Correction de l'affichage des alertes EPT dans le cockpit.

### Évolutions techniques
- Mise à jour de la configuration Cypress pour utiliser `cy.env` au lieu de `Cypress.env` et l'URL `SANDBOX_API_URL`.
- Refactorisation et correction des tests E2E pour s'adapter à la nouvelle version de Cypress (v15).
- Correction de l'appel de scripts JavaScript.
- Amélioration de la sécurité avec l'ajout de règles ASA et de la configuration CSP (Content Security Policy).
- Correction de la configuration Redis pour un redémarrage automatique.
- Mise à jour des dépendances `@emnapi` et suppression des entrées obsolètes esbuild.
- Migration des règles ASA vers l'absentéisme.
- Correction de l'algorithme de calcul du nombre de jours pour la projection du simulateur.
- Ajout de logs pour faciliter le débogage dans le cockpit.
- Correction de l'ordre de tri dans le cockpit.

### Autres changements
- Changement des fichiers de nomenclature. [#564](https://github.com/betagouv/a-just/issues/564)
- Correction de l'URL du collecteur d'extraction 2026.
- Ajout d'un fichier `.env.example` pour les tests end-to-end.
- Correction de la grammaire dans les logs.
- Suppression de bibliothèques inutilisées.
- Mise à jour du numéro de version pour la publication.
- Remplacement de l'ancien fichier extracteur-collecte par une nouvelle version.
- Correction du droit de mise à jour des juridictions CLE.
- Ajout de logs pour les erreurs.
- Correction de la date de début pour la vérification future.
- Ajout d'un message d'erreur pour le calcul du graphique de la vue du cockpit.
- Correction de la valeur de la plage lorsque c'est le premier jour du mois.
- Suppression de la migration ASA.
- Correction d'un bug lié à l'appel d'un script JS.
- Correction de l'affichage des catégories d'agents dans le simulateur.
- Correction d'un bug dans le calcul des jours d'indisponibilité.
- Ajout de commentaires pour faciliter la compréhension du code.
