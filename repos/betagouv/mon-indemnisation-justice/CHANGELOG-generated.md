## Changelog : mon-indemnisation-justice (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, l'application Mon Indemnisation Justice a connu des améliorations significatives concernant la gestion des dossiers, notamment pour les agents et les rédacteurs. Des correctifs ont été apportés aux trames de courriers et à la gestion des rejets, et des fonctionnalités ont été ajoutées pour faciliter la transmission des dossiers à FIP3 et la saisie des informations de virement. L'infrastructure a également été renforcée avec l'ajout d'un worker et l'amélioration du déploiement en staging.

### Évolutions fonctionnelles
- Les agents peuvent désormais saisir la date de virement.
- Possibilité pour les rédacteurs de transmettre les dossiers à FIP3 et de les marquer comme indemnisés. [#148](https://github.com/betagouv/mon-indemnisation-justice/pulls/148)
- Notification des rédacteurs lorsque l'arrêté est signé.
- Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours utilisateur.
- Amélioration de la prévisualisation des rejets et réorganisation des trames de rejet.
- Correction de l'affichage du bouton "Marquer indemnisé" qui était visible incorrectement. [#147](https://github.com/betagouv/mon-indemnisation-justice/pulls/147)
- Correction d'un bug empêchant l'envoi d'un formulaire si le bouton du SideMenu était cliqué.
- Correction de l'objet du courrier de décision.
- Amélioration de l'alignement de la modale de décision de rejet.

### Évolutions techniques
- Mise en place d'un worker pour exécuter les tâches cron via supervisor et docker.
- Déploiement des applications web et worker sur l'environnement "develop".
- Utilisation d'une image Docker spécifique pour la gestion de supervisor.
- Amélioration de la configuration de supervisor dans le dockerfile du worker.
- Utilisation d'un serveur OIDC mock pour les tests et le développement, avec des versions mises à jour pour supporter les redirect_uris et l'authentification basique.
- Ajout de `vite-plugin-node-polyfills` pour éviter les erreurs de conversion node -> browser.
- Déplacement des actions vers des routes API dédiées.
- Correction de l'ordre des migrations et configuration du reverse proxy pour l'environnement de staging.

### Autres changements
- Import des données des gendarmeries et des zones de compétence FDO.
- Nettoyage des motifs lors des clôtures.
- Mise à jour de la FAQ.
- Création d'un importeur CSV basique et d'une entité `EtablissementFDO`.
- Ajustement de l'en-tête.
- Correction du provisionnement des comptes agent en staging.
- Ajustement des trames de rejet.
- Relecture et amélioration des trames de l'arrêté de paiement et de la déclaration d'acceptation.
