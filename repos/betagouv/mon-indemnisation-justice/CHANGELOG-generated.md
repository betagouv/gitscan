## Changelog : mon-indemnisation-justice (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec les systèmes FIP3 et FDO, notamment pour la transmission des dossiers et la gestion des rejets. Des corrections et améliorations ont également été apportées à l'interface utilisateur pour faciliter le travail des agents et améliorer l'expérience utilisateur globale. Des travaux d'import de données et de gestion des établissements FDO ont été initiés.

### Évolutions fonctionnelles
- Possibilité pour l'agent de saisir la date de virement.
- Amélioration de la gestion des rejets : prévisualisation du rejet, réorganisation des trames de rejet, alignement de la modale de décision.
- Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours suivant.
- Notification du rédacteur lorsque l'arrêté est signé.
- Possibilité pour le rédacteur de transmettre le dossier à FIP3 et de le marquer comme indemnisé.
- Amélioration de la gestion des agents : création d'un onglet "Agents à valider", restriction d'accès pour les agents sans rôle DOSSIER, séparation des listes actifs/inactifs en onglets distincts.
- Possibilité de modifier les critères de recherche.
- Correction : la modale de rejet ne s'affiche plus si aucun courrier n'est présent.
- Correction : le bouton "Marquer indemnisé" est caché si le dossier n'est pas concerné.
- Correction : empêche le bouton du SideMenu de soumettre le formulaire.
- Correction : l'adresse peut être manquante sur un dossier.
- Correction : vite-plugin-static-copy en dépendance non dev.

### Évolutions techniques
- Utilisation de `pierrelemee/supervisor-docker` pour lancer et monitorer les tâches du worker.
- Déploiement des applications web et worker sur l'environnement "develop".
- Création d'une image Docker pour exécuter les tâches cron via supervisor.
- Ajout de `vite-plugin-node-polyfills` pour éviter les erreurs de conversion node -> browser.
- Déplacement des actions vers des routes API dédiées.
- Création d'un importeur CSV basique.
- Création de l'entité `EtablissementFDO`.
- Amélioration de la gestion des fichiers et des données.
- Ajout d'un test unitaire sur la route de suppression.
- Mise à jour des trames pour l'intégration avec FIP3.
- Gestion des erreurs FIP6 et FDO : capture, affichage et remontée des erreurs.

### Autres changements
- Ajustement de l'en-tête.
- Nettoyage des motifs lors des clôtures.
- Intégration en cours de la FAQ modifiée.
- Import des données des gendarmeries.
- Recalage des imports sur les fichiers CSV.
- Relecture et correction des tests.
- Mise à jour des trames de la déclaration d'acceptation et de l'arrêté de paiement.
- Figer la configuration de supervisor dans le dockerfile de worker.
- Création du point d'entrée API et appel depuis le DossierManager.
- Création de la modale de suppression de la pièce jointe (sans action réelle).
