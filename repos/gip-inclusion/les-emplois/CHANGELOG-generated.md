## Changelog : les-emplois (30 derniers jours, au 2026-08-20)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'intégration du module d'orientation, permettant une synchronisation fluide des données avec Dora. L'expérience utilisateur a été considérablement enrichie par de nouveaux filtres de recherche pour les candidats et une interface de double authentification (2FA) plus pédagogique. Parallèlement, des optimisations techniques importantes ont été réalisées pour améliorer la rapidité de l'application et la robustesse de la sécurité.

### Évolutions fonctionnelles
- **Module Orientation & Insertion :**
    - Mise en place d'une interface dédiée aux orientations avec vue détaillée, affichage en tableau et filtres avancés (par expéditeur, structure, statut et bénéficiaire).
    - Automatisation de la synchronisation des statuts d'orientation depuis Dora et ajout d'un outil d'importation de données.
    - Amélioration du suivi grâce à l'ajout de journaux de transition pour les orientations.
- **Gestion des Candidats :**
    - Enrichissement des capacités de filtrage (par conseiller, par membre d'organisation pour GEIQ/OPCS, et alerte sur la fin imminente du parcours IAE).
    - Ajout d'aides visuelles pour expliquer les champs en lecture seule et clarifier les informations relatives aux dates de contrat.
- **Expérience Utilisateur & Interface :**
    - Amélioration de la visibilité des contacts des conseillers et mise à jour des liens vers les formulaires de mise à jour de données ProConnect.
    - Optimisation de la gestion des transferts d'entreprises (déplacement automatique des évaluations GEIQ/OPCS).
    - Nettoyage des communications par email (suppression des mentions de sondages inutiles).
- **Sécurité & Authentification :**
    - Refonte du parcours de double authentification (OTP) : ajout d'exemples d'applications d'authentification via QR code, création d'un menu de configuration dédié et clarification des messages d'erreur.
    - Amélioration du flux de déconnexion pour FranceConnect.

### Évolutions techniques
- **Architecture & Performance :**
    - Refonte majeure du module `ft_connect` (renommage complet des modèles, des tables et des constantes pour une meilleure cohérence).
    - Optimisation significative des performances de la liste des candidats via la résolution de requêtes SQL redondantes (problème de N+1).
    - Refactorisation de la vue de détail des candidats pour une meilleure maintenabilité.
- **Gestion des Données & Sécurité :**
    - Introduction de la suppression logique (*soft-delete*) pour les services et les structures.
    - Renforcement de la sécurité des routes OTP (contrôle des accès basé sur les rôles et protection contre la manipulation de requêtes d'enrôlement).
- **Infrastructure & CI/CD :**
    - Optimisation des pipelines de déploiement avec une meilleure gestion du cache pour `setup-uv`.
    - Isolation des environnements de test et de développement via l'utilisation de buckets de stockage dédiés.

### Autres changements
- **Documentation :** Ajout de recommandations sur l'utilisation de gestionnaires de mots de passe et présentation de Podman comme alternative à Docker.
- **Maintenance :** Nettoyage général du code (suppression de tests et de templates inutilisés, renommage de variables) et corrections de nombreuses coquilles dans les messages de l'interface.
