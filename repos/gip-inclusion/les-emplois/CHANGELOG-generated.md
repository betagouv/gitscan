## Changelog : les-emplois (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la gestion des parcours usagers, notamment avec l'intégration de l'éligibilité RSA via l'API de la CAF et une refonte complète du suivi des modifications de dossiers salariés. La sécurité a été renforcée par un nouveau processus de réinitialisation de la double authentification (2FA), tandis que l'expérience des professionnels a été fluidifiée par de nouveaux outils de saisie et de support.

### Évolutions fonctionnelles
- **Sécurité & Accès** : Mise en place d'un processus complet de réinitialisation de la double authentification (2FA) incluant une traçabilité dans l'audit trail et une aide textuelle pour guider les utilisateurs vers les applications de sécurité.
- **Gestion des Usagers** : 
    - Intégration de l'éligibilité RSA directement dans les profils des demandeurs d'emploi.
    - Ajout du champ "Nationalité" et d'un onglet "Rendez-vous" sur les fiches usagers.
    - Création d'un formulaire de création d'usager simplifié au sein du tunnel d'orientation.
- **Support & Relation** : 
    - Nouveau système de rapports de support professionnel permettant aux employeurs de solliciter l'aide des prescripteurs.
    - Intégration du widget Zendesk pour l'aide en ligne (affichage conditionnel selon le consentement).
- **Interface & Expérience Utilisateur** : 
    - Amélioration de la saisie des fonctions pour les professionnels (suggestions, copie de champs, gestion de l'affichage des multiples appartenances).
    - Optimisation visuelle globale : nouveau design de l'écran de connexion, mise à jour du thème et optimisation du poids des images.
    - Ajout de bannières d'information contextuelles (campagnes DORA, alertes de fin de contrat).

### Évolutions techniques
- **Workflow Salarié** : Refonte majeure de la gestion des modifications de dossiers (nouveaux états de transition, gestion automatisée des doublons, traitement des rejets et amélioration des notifications).
- **Données Géographiques (ASP)** : Amélioration de la synchronisation des communes avec une gestion intelligente des exceptions pour les territoires d'outre-mer et mise en cache des résultats de recherche.
- **Suivi des Échanges** : Implémentation d'un système de suivi des emails de mise en relation via un webhook (inbound parsing) pour assurer la traçabilité des échanges.
- **Infrastructure & CI/CD** : 
    - Optimisation des pipelines de déploiement (gestion des caches pour les bibliothèques spatiales, utilisation de `uv`).
    - Amélioration de la robustesse des tests (isolation des appels réseau, gestion du temps pour les tests de calendrier).
- **Performance** : Migration vers `python-calamine` pour un traitement plus performant des fichiers Excel.

### Autres changements
- **Documentation & Légal** : Mise à jour des conditions générales d'utilisation et de la politique de confidentialité.
- **Maintenance** : Nettoyage important du code source par la suppression de nombreuses fonctions, commandes et helpers inutilisés.
- **Configuration** : Optimisation de la gestion des variables d'environnement (Redis) et des paramètres de suivi (Matomo).
