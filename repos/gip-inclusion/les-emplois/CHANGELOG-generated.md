## Changelog : les-emplois (30 derniers jours, au 06 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes pour améliorer l'accompagnement des usagers, notamment via une meilleure gestion des fins de parcours et l'ajout d'informations clés (nationalité, badges QPV). Les outils pour les professionnels ont été enrichis avec un nouveau système de rapports de support. Parallèlement, une montée de version majeure (Python 3.14) et des optimisations de performance sur l'interface d'administration assurent une plateforme plus robuste et rapide.

### Évolutions fonctionnelles
- **Orientation et suivi des usagers** : 
    - Ajout des champs nationalité et âge dans les profils et formulaires.
    - Intégration de badges QPV pour une meilleure identification géographique.
    - Amélioration du tunnel d'orientation avec des formulaires simplifiés et l'affichage d'informations complémentaires sur les bénéficiaires.
    - Mise en place de fonctionnalités dédiées aux fins de parcours (filtres spécifiques, demandes de support automatisées et affichage des situations de fin de contrat).
- **Outils pour les professionnels et entreprises** :
    - Création d'un système de rapports de support professionnel avec notifications pour les prescripteurs autorisés.
    - Amélioration de la visibilité des contrats et des informations de recherche pour les employeurs.
    - Nouvelle vue pour lister les organisations des territoires.
- **Interface et expérience utilisateur (UI/UX)** :
    - Refonte visuelle de la page de connexion (nouveau design, illustrations et couleurs).
    - Harmonisation des composants graphiques (boutons, badges, alertes) sur l'ensemble de la plateforme.
    - Amélioration de la clarté des messages d'erreur et des instructions dans les formulaires.
- **Pilotage et données** :
    - Enrichissement des exports Metabase (ajout des codes INSEE, suivi des emails de mobilisation et présence de numéros de téléphone).

### Évolutions techniques
- **Performance et Administration** :
    - Optimisation de l'affichage des grandes tables dans l'interface d'administration (utilisation de pagination et de hiérarchies de dates optimisées).
    - Réduction de la charge des requêtes sur les pages d'administration volumineuses.
- **Infrastructure et Backend** :
    - Migration du système de stockage de MinIO vers RustFS.
    - Passage à Python 3.14.
    - Amélioration de la résilience de la gestion des tâches (reconnexion automatique à Redis pour Huey).
- **Gestion des données et géographie** :
    - Optimisation du processus de synchronisation des communes (mise en cache des résultats, meilleure gestion des erreurs CSV et détection précoce des incohérences).
    - Amélioration de la précision du géocodage.
- **Sécurité et Fiabilité** :
    - Renforcement de la validation des adresses email via la vérification des serveurs MX.
    - Amélioration du processus d'enrôlement à la double authentification (2FA).
    - Optimisation de la traçabilité (audit trail) et de la gestion des logs d'erreurs d'envoi d'emails.
- **Qualité logicielle et CI/CD** :
    - Accélération de la chaîne d'intégration continue (tests parallélisés et mise en cache des bibliothèques spatiales).
    - Stabilisation de la suite de tests (correction de tests instables/flaky).

### Autres changements
- **Documentation** : Mise à jour des mentions légales (CGU et politique de confidentialité) et ajout de la documentation technique sur le parsing des emails entrants.
- **Maintenance** : Nettoyage de code, suppression de fichiers statiques et de commandes de gestion inutilisées.
