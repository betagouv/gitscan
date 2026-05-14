## Changelog : aides-agri (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la préparation et le déploiement de la version 2 du parcours agri, avec de nombreuses corrections et améliorations de l'interface utilisateur et de la gestion des données. Des améliorations ont également été apportées à l'administration des aides, à la gestion des logos des DDT(M) et à la stabilité globale de l'application.

### Évolutions fonctionnelles
- **Parcours agri v2 :** Déploiement de la nouvelle version du parcours utilisateur pour les exploitants agricoles [#418](https://github.com/betagouv/aides-agri/pull/418).
- **Filtres d'aides :** Correction d'un bug d'alignement des filtres sur la page d'ensemble des aides [#515](https://github.com/betagouv/aides-agri/issues/515).
- **Page d'aide :** Améliorations mineures de la page d'aide [#543](https://github.com/betagouv/aides-agri/issues/543).
- **Homepage :** Possibilité de sélectionner toutes les filières sur la page d'accueil [#531](https://github.com/betagouv/aides-agri/issues/531).
- **Aides réservées :** Ajout d'une information sur les aides réservées aux groupements de producteurs [#538](https://github.com/betagouv/aides-agri/issues/538).
- **Base juridique des aides :** Consolidation de la gestion de la base juridique des aides [#495](https://github.com/betagouv/aides-agri/issues/495) et [#499](https://github.com/betagouv/aides-agri/issues/499).
- **Export CSV :** Ajout de la raison de désactivation à l'export CSV de l'administration [#532](https://github.com/betagouv/aides-agri/issues/532).
- **Logos DDT(M) :** Scripts de création et d'association des logos des Directions Départementales des Territoires et de la Mer [#493](https://github.com/betagouv/aides-agri/issues/493).

### Évolutions techniques
- **Déploiement automatisé :** Améliorations et corrections successives du processus de déploiement automatisé [#548](https://github.com/betagouv/aides-agri/issues/548), [#550](https://github.com/betagouv/aides-agri/issues/550), [#551](https://github.com/betagouv/aides-agri/issues/551), [#552](https://github.com/betagouv/aides-agri/issues/552), [#553](https://github.com/betagouv/aides-agri/issues/553), [#554](https://github.com/betagouv/aides-agri/issues/554).
- **Performance :** Tentatives de réduction des latences de l'application et de limitation des fuites mémoire [#523](https://github.com/betagouv/aides-agri/issues/523), [#537](https://github.com/betagouv/aides-agri/issues/537).
- **Base de données :** Correctif sur le réglage de la connexion persistante à la base de données [#536](https://github.com/betagouv/aides-agri/issues/536) et facilitation du déploiement en cas de changement de schéma [#501](https://github.com/betagouv/aides-agri/issues/501).
- **Notifications :** Améliorations des notifications internes [#547](https://github.com/betagouv/aides-agri/issues/547).
- **Accessibilité :** Amélioration de l'accessibilité de la validation de formulaire côté client [#530](https://github.com/betagouv/aides-agri/issues/530).
- **Scripts de stress-test :** Ajout d'un script de stress-test de performance de l'infrastructure [#544](https://github.com/betagouv/aides-agri/issues/544).

### Autres changements
- **Documentation :** Mise à jour de la date de validité du fichier security.txt [#505](https://github.com/betagouv/aides-agri/issues/505).
- **Corrections mineures :** Correction d'un bug sur le fil d'Ariane [#541](https://github.com/betagouv/aides-agri/issues/541), d'un bug d'affichage de couleur [#511](https://github.com/betagouv/aides-agri/issues/511), et de l'impression PDF [#525](https://github.com/betagouv/aides-agri/issues/525).
- **Administration :** Correction du crash de l'historique dans l'administration [#524](https://github.com/betagouv/aides-agri/issues/524) et améliorations générales de l'outil d'édition des aides [#498](https://github.com/betagouv/aides-agri/issues/498).
- **Tracking :** Ajout de tracking d'événement de clic sur lien externe pour le mode minimal [#535](https://github.com/betagouv/aides-agri/issues/535).
- **Corrections de slug :** Correction du slug des Aides [#497](https://github.com/betagouv/aides-agri/issues/497).
