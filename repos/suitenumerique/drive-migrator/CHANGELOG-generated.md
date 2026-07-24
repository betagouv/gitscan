## Changelog : drive-migrator (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à la gestion des utilisateurs et à l'expérience utilisateur globale. L'authentification avec Resana a été renforcée avec l'ajout de la double authentification (MFA). Des correctifs ont été apportés pour améliorer la stabilité et la fiabilité du processus de migration, notamment en gérant mieux les limites de fichiers et en corrigeant des erreurs d'accès. L'interface utilisateur a également été modernisée et des pages d'état ont été ajoutées.

### Évolutions fonctionnelles
- Ajout d'une page pour télécharger les archives de migration, accessible uniquement aux utilisateurs authentifiés.
- Implémentation d'un mode restreint pour les nouveaux comptes utilisateurs, nécessitant une validation par un administrateur.
- Ajout d'une page d'état "compte en attente" pour les utilisateurs en mode restreint.
- Amélioration de l'affichage des informations sur les limites de fichiers lors de la migration.
- Possibilité de limiter le nombre de fichiers migrés par espace de travail via une configuration.
- Intégration de la double authentification (MFA) pour l'authentification Resana via Keycloak.
- Pré-remplissage et verrouillage du champ d'email Resana avec le compte Proconnect.
- Ajout d'une option pour inclure la liste des utilisateurs partagés lors de l'export vers Drive.
- Amélioration de l'interface utilisateur du tableau de bord et de la page d'authentification.
- Ajout d'un favicon pour une meilleure identification visuelle.
- Correction de l'affichage des messages vides.
- Amélioration de la présentation de la modale de partage.

### Évolutions techniques
- Utilisation de GitHub-hosted runners pour l'exécution des workflows CI/CD.
- Mise à jour des dépendances de sécurité, notamment pytest (v9).
- Amélioration de la configuration Docker pour éviter les avertissements.
- Mise à jour de la version de Python (3.14.6) et des dépendances Python.
- Ajout de tests de sécurité avec Zizmor.
- Correction de problèmes liés à l'injection de variables d'environnement dans les conteneurs Docker.
- Refactoring du code pour utiliser une méthode générique pour l'envoi des emails.
- Utilisation de `ruff` pour le formatage du code source et du backend drive.
- Ajout d'un script pour générer des données de démonstration pour le backend filesystem.
- Utilisation de l'environnement `FRONTEND_THEME=dsfr` pour le build du frontend.
- Correction de problèmes liés à la configuration OIDC pour un setup Keycloak en standalone.
- Suppression de Crisp et refonte de l'interface utilisateur.

### Autres changements
- Mise à jour de la documentation README avec une section "Getting Started" améliorée.
- Ajout d'une cible `frontend-lint` pour effectuer des vérifications de style sur le frontend.
- Correction de l'échappement des entités HTML dans les noms Resana.
- Suppression de clés inutilisées dans le projet.
- Mise à jour des variables communes pour le thème Cunningham (dsfr).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de labels aux backends source.
- Correction de l'importation manquante dans les tests.
- Correction d'erreurs ESLint dans le frontend.
- Ajout de la construction pour une seule architecture Docker.
