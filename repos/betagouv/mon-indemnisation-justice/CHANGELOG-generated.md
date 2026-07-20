## Changelog : mon-indemnisation-justice (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'intégration avec les systèmes FIP3 et FDO, notamment pour la transmission des dossiers et la gestion des rejets. Des corrections et des ajustements ont également été apportés aux trames de courriers et d'arrêtés, ainsi qu'à l'interface utilisateur pour une meilleure expérience des agents et des utilisateurs. Des travaux d'import de données et de gestion des établissements FDO ont été entrepris.

### Évolutions fonctionnelles
- Les agents peuvent désormais saisir la date de virement sur les dossiers.
- Possibilité pour le rédacteur de transmettre les dossiers à FIP3 et de les marquer comme indemnisés. [#148](https://github.com/betagouv/mon-indemnisation-justice/pull/148)
- Notification du rédacteur lors de la signature de l'arrêté.
- Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours utilisateur.
- Amélioration de la modale de décision de rejet pour une meilleure cohérence.
- Prévisualisation des rejets désormais possible.
- Possibilité de modifier les critères de recherche des dossiers.
- Création d'un onglet dédié aux "Agents à valider" avec restriction d'accès.
- Séparation des listes d'agents actifs et inactifs en deux onglets distincts.
- Correction : L'adresse n'est plus obligatoire sur un dossier.

### Évolutions techniques
- Mise en place d'un worker pour exécuter les tâches cron via supervisor et docker. [#4637283](https://github.com/betagouv/mon-indemnisation-justice/commit/4637283)
- Utilisation de `pierrelemee/supervisor-docker` pour le lancement et la supervision des tâches du worker.
- Déploiement des applications web et worker sur l'environnement "develop".
- Création d'un importeur CSV basique pour faciliter l'import de données.
- Création de l'entité `EtablissementFDO` pour la gestion des établissements.
- Ajout de `vite-plugin-node-polyfills` pour résoudre les erreurs de conversion Node -> Browser.
- Correction : Suppression d'une dépendance de développement inutile (`vite-plugin-static-copy`).
- Amélioration de la gestion des erreurs lors des appels aux APIs FIP6 et FDO, avec affichage et remontée des erreurs.
- Refactorisation : Déplacement des actions vers des routes API dédiées.
- Refactorisation : Alignement des trames de rejet.
- Refactorisation : Relecture et mise à jour des trames de PI, déclaration d'acceptation et arrêtés de paiement.
- Ajout d'un test unitaire pour la route de suppression de pièces jointes.

### Autres changements
- Nettoyage des motifs lors des clôtures de dossiers.
- Mise à jour de la FAQ.
- Correction de l'objet du courrier de décision.
- Correction : Empêcher le bouton du SideMenu de soumettre le formulaire.
- Correction : Figer la configuration de supervisor dans le Dockerfile du worker.
- Correction : Eviter l'appel API pour les compteurs de dossiers pour les agents sans rôle DOSSIER.
- Correction : Correction des tests unitaires.
- Correction : Correction d'un problème avec `react-pdf`.
- Amélioration de la gestion des fichiers et des données.
