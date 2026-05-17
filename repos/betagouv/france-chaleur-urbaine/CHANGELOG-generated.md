## Changelog : france-chaleur-urbaine (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des permissions, l'optimisation des performances et l'ajout de nouvelles fonctionnalités pour faciliter l'administration et l'utilisation de la plateforme. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant les formulaires et l'intégration avec Ademe Connect.

### Évolutions fonctionnelles
- Intégration d'Ademe Connect pour l'authentification des utilisateurs.
- Ajout d'un nouveau système de permissions, incluant des rôles (CCRT, ALEC) et une gestion plus fine des accès.
- Amélioration du workflow d'affectation des demandes au réseau.
- Ajout d'un bouton de réinitialisation sur les formulaires.
- Mise à jour de la FAQ avec de nouvelles questions et réponses.
- Ajout d'un message d'information lors de la soumission du formulaire de collecte de contact pour les non-raccordables.
- Ajout d'un bandeau d'information concernant une future indisponibilité du service.
- Affichage des demandes plutôt que des tests d'adresses dans l'admin des réseaux.
- Ajout d'une commande pour analyser des réseaux.
- Ajout d'une commande pour mettre à jour les réseaux via un répertoire.
- Ajout d'un script de migration des notes de tags.
- Ajout d'un lien pour corriger les permissions d'un gestionnaire.
- Affichage des compteurs d'accès aux demandes avec détail.
- Amélioration des relances et ajout de notes.
- Refonte des emails et affichage dans l'admin.

### Évolutions techniques
- Mise en cache des tuiles pour améliorer les performances de la carte.
- Refactoring et simplification de `demands-service`.
- Optimisation du rendu de la carte.
- Amélioration des performances du listing des demandes.
- Ajout d'un module de métriques avec une API Prometheus.
- Mise à jour des dépendances et refactoring du code.
- Suppression de code obsolète et nettoyage du codebase.
- Amélioration du typage du code.
- Utilisation de helpers HTTP pour une meilleure gestion des requêtes.
- Utilisation des variables d'environnement via une configuration centralisée.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de fichiers inutiles.
- Mise à jour des statistiques mensuelles.
- Suppression de tables Airtable inutilisées.
- Ajout de commentaires et documentation pour faciliter la maintenance du code.
- Ajout d'un script pour dropper des tables à distance.
- Correction de l'affichage des permissions réseaux en construction.
- Ajout d'un dashboard sur la cohérence des données.
- Factorisation des fonctions de recherche de réseau.
- Suppression du bandeau de mise à jour.
- Identification améliorée des événements liés aux demandes.
- Tri des emails selon le domaine puis préfixe.
- Ajout du rôle CCRT.
- Affichage des rôles complets dans la colonne Accès.
- Maj FAQ gestionnaire.
- Nettoyage et fix événements custom.
- Fix maj demandes par utilisateur non authentifié.
- Regroupement des couleurs des rôles.
- Maj onglets presets selon profils.
- Suppression du fichier `.claude/`.
- Renvoi du body dans les erreurs fetch.
- Rendre les modals deprecated.
- Envoi des mails aux gestionnaires selon permission réseau.
- Fix formulaire création utilisateur par un admin.
- Fix création demande.
- Ajout de permissions en masse via ids & sncu.
- Fix labels.
- Enregistrement de l'entreprise de l'utilisateur.
- Refacto/simplification autour des types d'entités.
- Affichage mention aucun résultat dans les autocomplete.
- Fix lien réseaux->stats vers les demandes.
- Statut non réalisable pour demandes non éligibles.
- Affichage de la colonne has_PDP dans l'admin.
- Refactor les emails et les affiche dans l'admin.
- Fix la recherche par id sncu dans la page stats.
- Track d'autres events.
- Migre les comptes métropoles.
- Track la maj des id pdp.
- Ajoute ALEC à la structure + raccourcis de sélection role.
- Track les maj des réseaux.
- ai: maj automatique des docs des modules.
- ai: inférence, 1 instruction / ligne, ternaires.
- ai: pratiques exports et nommage variables.
- ai: utilise un import pour que claude charge systématiquement AGENTS.md
- ai: maj les pratiques.
- ai: utilise les helpers HTTP.
- ai: utilise les variables d'env via config.
- ai: supprime la liste des modules en dur.
- ai: précise le format attendu des migrations.
- ai: pas de conditions useless.
- ai: précision ne pas surcharger staleTime.
- ai: feedback toujours dans le projet.
- ai: corrige l'usage de db:sync pour les typages.
- Agrège les permissions à la liste des users.
- Fix impersonation depuis l'écran des utilisateurs.
- Sauvegarde le preset sélectionné dans l'URL /pro/demandes.
- Ne ferme pas la popup lors des clics dans les tags.
- Events de maj de permission.
- Complète les tests des routes territoires.
- Supprime les presets haut potentiel et dans pdp.
- Améliore la validation route impersonate.
- Déplace les demandes à traiter en 1er et par défaut.
