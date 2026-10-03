## Changelog : reva (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois-ci, les évolutions ont principalement porté sur l'enrichissement du module **VAE Collective** avec l'introduction des "sous-comptes", permettant une gestion plus granulaire des droits d'accès. La sécurité a été renforcée par le déploiement de la double authentification (2FA) et l'expérience utilisateur a été améliorée grâce à la création de nouveaux tableaux de bord pour les administrateurs et les gestionnaires de registre.

### Évolutions fonctionnelles

**VAE Collective & Sous-comptes**
- Introduction des **sous-comptes** : possibilité de connexion dédiée, gestion des paramètres et interface spécifique pour les sous-comptes.
- Gestion fine des droits : création d'une page "Droits d'accès" et de composants permettant de définir des rôles spécifiques par cohorte (lecture, modification, création).
- Amélioration de la navigation : ajout d'une barre de recherche pour les listes de sous-comptes et gestion des permissions de visibilité des cohortes.

**Expérience Candidat**
- Flexibilité des certifications : les candidats peuvent désormais choisir leur certification pour les VAE collectives proposant plusieurs options.
- Parcours dématérialisé : amélioration du flux de candidature autonome permettant de modifier les objectifs et expériences si le dossier est incomplet.
- Corrections diverses : correction de liens dans les pages de rendez-vous et amélioration de la clarté des libellés.

**Administration & Pilotage**
- Nouveaux tableaux de bord : mise à disposition d'interfaces de pilotage pour les comptes de certification locale et les gestionnaires de registre.
- Pilotage des cohortes : ajout d'une carte indiquant le nombre de candidatures directement sur la page de la cohorte.
- Gestion des dossiers : ajout de filtres pour visualiser les candidatures actives pour les organismes (AAP).

### Évolutions techniques

**Sécurité & Authentification**
- **Double authentification (2FA)** : activation de la 2FA par email pour les comptes de la VAE Collective.
- **Refonte de l'autorisation** : migration des vérifications d'autorisation "inline" vers un système de politiques (`withPolicies`) pour une meilleure sécurité et maintenabilité.
- **Gestion des rôles** : optimisation de la gestion des rôles via l'utilisation des types de rôles Keycloak plutôt que de simples chaînes de caractères.

**API & Données**
- **Nouveau modèle métier** : introduction d'un objet "accompagnement" pour dissocier la notion de suivi de la candidature elle-même.
- **Migration API** : passage de l'API France Compétences RNCP de la version 2 à la version 4.
- **Base de données** : ajout du champ `lastLoginAt` pour le suivi des connexions et implémentation d'une relation many-to-many pour les comptes de certification locale.
- **Anonymisation** : ajout d'un script pour l'anonymisation complète de la base de données.

**Infrastructure**
- Mise à jour de l'image Docker de **Keycloak** et correction des buildpacks pour l'environnement de déploiement.
- Ajustements de la configuration **Traefik** concernant la réinitialisation des mots de passe.

### Autres changements
- Nettoyage du code (suppression d'imports inutilisés).
- Renommage de contraintes de clés étrangères dans la base de données.
- Mise à jour des scripts de notification par email pour les organismes.
