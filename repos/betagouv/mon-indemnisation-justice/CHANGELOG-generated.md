## Changelog : mon-indemnisation-justice (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, l'application Mon Indemnisation Justice a bénéficié d'améliorations significatives concernant la gestion des agents, l'intégration de données FDO, la gestion des courriers et des trames associées, ainsi que des corrections et optimisations techniques pour améliorer la stabilité et la performance de la plateforme. Des travaux ont été réalisés pour préparer le déploiement en staging et faciliter l'automatisation des tâches.

### Évolutions fonctionnelles
- Possibilité pour les agents du Ministère de l'Intérieur d'être automatiquement exemptés d'affectation.
- Ajout de la possibilité pour le rédacteur de saisir la date de virement.
- Extension des tableaux de bord de liaison FIP3 aux réacteurs.
- Le rédacteur peut maintenant transmettre les dossiers à FIP3 et marquer le dossier comme indemnisé.
- Notification du rédacteur lorsque l'arrêté est signé.
- Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours utilisateur.
- Prévisualisation du rejet possible pour l'agent.
- Amélioration de la modale de décision de rejet pour une meilleure cohérence.
- Correction : le bouton pour marquer un dossier comme indemnisé est maintenant caché si le dossier n'est pas concerné.
- Correction : adaptation de l'objet du courrier de décision.
- Correction : modale de rejet fonctionnelle même en l'absence de courrier.

### Évolutions techniques
- Mise en place d'un serveur OIDC mock pour faciliter les tests et le développement.
- Utilisation de `pierrelemee/supervisor-docker` pour lancer et monitorer les tâches du worker.
- Déploiement des applications web et worker sur l'environnement "develop".
- Création d'une image Docker pour l'exécution des tâches cron via supervisor.
- Amélioration de la gestion des fichiers et des données.
- Correction de l'ordre des migrations et du reverse proxy en staging.
- Correction des scripts de démarrage en staging.
- Ajout de logs pour faciliter le débogage des erreurs OIDC.
- Ajout de polyfills Node.js pour éviter les erreurs de conversion navigateur.
- Refonte de la structure des routes API pour séparer les actions.
- Correction d'un bug empêchant la soumission du formulaire par le bouton du SideMenu.
- Ajout de tests unitaires et fonctionnels.
- Purge des données avant migration en environnement de développement.
- Validation du mapping Doctrine lors des tests.
- Correction d'un problème de provisionnement des comptes agent en staging.

### Autres changements
- Intégration de la FAQ mise à jour.
- Mise à jour des trames de courrier (PI, déclaration d'acceptation, arrêtés de paiement et de rejet).
- Nettoyage des motifs lors des clôtures.
- Correction d'un bug lié à l'import des données des zones de compétence FDO.
- Correction d'un bug lié à l'import des données des gendarmeries.
- Correction pour gérer les communes sans département (TOM).
- Configuration de supervisor figée dans le Dockerfile du worker.
- Ajustement de l'en-tête.
- Importateur CSV basique implémenté.
- Création de l'entité EtablissementFDO.
