## Changelog : rdv-service-public (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à rdv-service-public au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur, des optimisations de performance et des mises à jour de sécurité. Des efforts ont été faits pour améliorer la gestion des rendez-vous collectifs, la synchronisation CalDAV et l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Possibilité de notifier les usagers d'un changement de lien de visioconférence (#6184).
- Ajout d'un bouton "Ajouter à mon agenda" sur l'écran de confirmation de rendez-vous (#6190).
- Amélioration de l'affichage des erreurs lors de la saisie d'un code de connexion (#6062).
- Permettre l'annulation d'une participation à un RDV collectif à l'initiative du service (#6127).
- Amélioration de l'affichage des prescripteurs sur les RDV collectifs (#6147, #6124).
- Correction de l'apparition de la recherche des plages d'ouvertures (#6054).
- Amélioration de la page d'accueil (#6084).
- Correction de la fermeture d'une organisation lorsqu'on est le dernier administrateur de territoire (#6063).
- Ajout de la possibilité de reprendre une migration inter-instance après une interruption (#6065).
- Correction de la synchronisation Caldav en cas de changement de la transparence (#6075).
- Amélioration de l'affichage des détails des rendez-vous (#6107).

### Évolutions techniques
- Migration de Webpack vers esbuild pour améliorer les performances de build (#6163).
- Passage à Yarn v4 (#6064).
- Mise à jour de FullCalendar de la version 5 à la version 6 (#6080).
- Refactorisation de l'authentification et renforcement des CSP pour une meilleure sécurité (#6156, #6157).
- Amélioration de la gestion des erreurs et ajout de logs pour faciliter le débogage (#6180, #6104, #6066).
- Optimisation des requêtes et de la gestion de la mémoire pour améliorer la performance générale (#6115, #6114, #6118, #6095).
- Suppression de code obsolète et nettoyage de la base de données (#6185, #6177, #6167, #6093, #6076).
- Amélioration de l'outillage pour les instances multiples en local (#6143, #6129).

### Autres changements
- Suppression de la documentation et du code liés à l'inscription des utilisateurs (#6014).
- Mise à jour de la source des articles de blog vers docs.numerique.gouv.fr (#6024).
- Correction de plusieurs petites erreurs et améliorations de la qualité du code (#6199, #6200, #6197, #6196, #6194, #6192, #6191, #6189, #6188, #6187, #6186, #6183, #6182, #6181, #6179, #6178, #6176, #6175, #6174, #6173, #6171, #6170, #6169, #6168, #6166, #6165, #6162, #6161, #6160, #6155, #6154, #6153, #6151, #6150, #6149, #6148, #6146, #6145, #6144, #6142, #6141, #6140, #6139, #6138, #6137, #6136, #6135, #6134, #6133, #6132, #6130, #6126, #6125, #6124, #6123, #6122, #6120, #6119, #6117, #6116, #6113, #6112, #6111, #6110, #6109, #6108, #6106, #6105, #6103, #6102, #6101, #6100, #6099, #6098, #6097, #6096, #6095, #6094, #6092, #6091, #6090, #6089, #6088, #6087, #6086, #6085, #6083, #6082, #6081, #6080, #6079, #6078, #6077, #6076, #6075, #6074, #6073, #6072, #6071, #6070, #6069, #6068, #6067, #6066, #6065, #6064, #6063, #6062, #6061, #6060, #6059, #6057, #6056, #6055, #6054, #6053, #6051, #6050, #6049, #6037).
