## Changelog : mon-indemnisation-justice (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce changelog couvre une période d'améliorations significatives sur l'application Mon Indemnisation Justice, notamment des avancées majeures dans le traitement des dossiers liés aux dysfonctionnements, l'intégration de nouvelles données (établissements FDO), et des corrections d'interface utilisateur pour améliorer l'expérience des agents. Des efforts ont également été déployés pour stabiliser l'environnement de staging et améliorer la gestion des tâches asynchrones.

### Évolutions fonctionnelles
- Ajout de la possibilité pour l'agent de saisir la date de virement.
- Extension des tableaux de bord de liaison avec FIP3 aux réacteurs.
- Permettre au rédacteur de transmettre les dossiers à FIP3 et de les marquer comme indemnisés.
- Notification du rédacteur lorsque l'arrêté est signé.
- Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours utilisateur.
- Amélioration de la modale de décision de rejet pour une meilleure cohérence.
- Ajout de boutons de navigation (annuler, précédent, retour à l'accueil) au test d'éligibilité dysfonctionnement et révision de la mise en page.
- Possibilité de prévisualiser le rejet d'une demande.
- Correction : cacher le bouton pour marquer indemnisé si le dossier n'est pas encore concerné.
- Correction : adapter l'objet du courrier de décision.
- Correction : modale de rejet bloquée si aucun courrier n'est présent.

### Évolutions techniques
- Mise en place d'un worker pour exécuter les tâches asynchrones via `supervisor` et `docker`, améliorant la fiabilité et la scalabilité.
- Utilisation d'une image `pierrelemee/mock-oidc-server` pour faciliter les tests d'authentification.
- Déploiement des applications web et worker sur l'environnement `develop`.
- Amélioration de la gestion des fichiers et des données, notamment avec un importeur CSV basique.
- Ajout de `vite-plugin-node-polyfills` pour corriger les erreurs JavaScript liées à la conversion node -> browser.
- Refonte des routes API pour les actions, les déplaçant vers des endpoints dédiés.
- Nettoyage des motifs lors des clôtures de dossiers.
- Correction de l'ordre des migrations et du reverse proxy en staging.

### Autres changements
- Import des données des gendarmeries et des établissements FDO.
- Mise à jour des trames de documents (PI, déclaration d'acceptation, arrêtés de paiement, rejets).
- Intégration de la FAQ modifiée.
- Correction du comportement du bouton du SideMenu qui soumettait le formulaire.
- Provisionnement des comptes agent en staging corrigé.
- Correction de l'import des zones de compétence FDO.
- Ajustement de l'en-tête.
- Correction de la configuration de supervisor dans le dockerfile du worker.
