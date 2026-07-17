## Changelog : mon-indemnisation-justice (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives concernant la gestion des données, notamment l'import de données de gendarmeries et d'établissements FDO. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier sur les formulaires et la gestion des erreurs. L'application a également été optimisée pour mieux gérer les accès et les rôles des agents.

### Évolutions fonctionnelles
- Ajout de l'option "bailleur social" au test d'éligibilité et adaptation du parcours utilisateur associé.
- Amélioration de la gestion des fichiers et des données.
- Possibilité de modifier les critères de recherche.
- Séparation des listes d'agents actifs et inactifs en deux onglets distincts.
- Création d'un onglet "Agents à valider" pour faciliter la gestion des accès.
- Correction du fonctionnement de la modale de mot de passe oublié.
- Fluidification de l'affichage des champs et possibilité de masquer les outils Tanstack.
- Gestion des erreurs FIP6 et FDO : affichage et remontée des erreurs.
- Suppression de l'affichage de la quittance subrogative pour les bailleurs sociaux.
- Correction d'un bug empêchant le bouton du SideMenu de soumettre le formulaire.
- Correction pour permettre l'affichage correct de PDF sur Safari iOS [#c83cf05](https://github.com/betagouv/mon-indemnisation-justice/commit/c83cf05).

### Évolutions techniques
- Intégration de `vite-plugin-node-polyfills` pour résoudre les erreurs de conversion Node.js vers navigateur.
- Utilisation de `pierrelemee/supervisor-docker` pour lancer et monitorer les tâches du worker.
- Création d'une image Docker pour exécuter les tâches cron via supervisor.
- Déploiement des applications web et worker sur l'environnement "develop".
- Création d'un importeur CSV basique.
- Création de l'entité `EtablissementFDO`.
- Création d'un point d'entrée API et appel depuis le `DossierManager`.
- Ajout d'un test unitaire sur la route de suppression.
- Correction de la dépendance `vite-plugin-static-copy` pour qu'elle ne soit pas une dépendance de développement.
- Correction pour gérer le cas où l'adresse est manquante sur un dossier.
- Correction pour éviter un appel API inutile pour les compteurs de dossiers pour les agents sans rôle DOSSIER.
- Restriction de l'accès à l'agent MJ sans rôle AGENT_DOSSIER.
- Figer la configuration de supervisor dans le dockerfile du worker.

### Autres changements
- Intégration de la FAQ modifiée (en cours).
- Recalage des imports sur les fichiers CSV (en cours).
- Création d'une modale de suppression de pièce jointe (sans action réelle pour le moment).
- Correctifs pour la librairie `react-pdf`.
