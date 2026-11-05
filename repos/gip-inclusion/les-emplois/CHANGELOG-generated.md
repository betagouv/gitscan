## Changelog : les-emplois (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes tant sur l'expérience utilisateur que sur sa robustesse technique. Les professionnels bénéficient de nouveaux outils de pilotage (rapports de support, statistiques GEIQ) et les usagers d'un parcours d'orientation plus fluide et enrichi (ajout de la nationalité, badge QPV, demandes d'accompagnement en fin de parcours). Côté infrastructure, le passage à Python 3.14 et l'adoption de RustFS renforcent la modernité et la performance du service.

### Évolutions fonctionnelles
- **Parcours Usager & Orientation** : 
    - Ajout du champ "Nationalité" et du badge "QPV" sur les profils usagers.
    - Amélioration du tunnel d'orientation avec un formulaire de création simplifié et un affichage plus complet des informations sur les bénéficiaires.
    - Mise en place d'un système de demande de support professionnel lorsqu'un contrat arrive à échéance.
- **Outils de Pilotage & Administration** :
    - Création de nouveaux tableaux de bord pour le suivi des dossiers salariés et l'évaluation des campagnes GEIQ.
    - Amélioration des exports Metabase (ajout des codes INSEE, rapports de support pro et suivi des emails de mobilisation).
    - Meilleure gestion des organisations et des contrats ASP dans l'interface d'administration.
- **Interface Utilisateur (UI)** :
    - Harmonisation visuelle globale (tailles des badges, couleurs des boutons, styles des sections d'informations).
    - Refonte de l'écran de connexion (nouvelle illustration et design).
    - Ajout de bannières d'information contextuelles (campagnes DORA, informations NIR).

### Évolutions techniques
- **Infrastructure & Performance** :
    - Migration majeure vers Python 3.14.
    - Remplacement de MinIO par RustFS pour le stockage.
    - Optimisation des performances de l'administration (pagination et chargement des pages sur les grandes tables) et compression des ressources images.
- **Gestion des Données & Imports** :
    - Refonte du processus de synchronisation des communes (mise en cache, détection précoce des incohérences CSV, gestion des contraintes de lieu de naissance).
    - Amélioration de la robustesse des imports (gestion des fichiers Excel via `python-calamine`, rejet des fichiers corrompus).
    - Optimisation du traitement des emails entrants via l'intégration de webhooks authentifiés (Brevo).
- **Sécurité & Authentification** :
    - Amélioration du parcours d'enrôlement à la double authentification (2FA).
    - Renforcement de la validation des adresses email (vérification des serveurs MX) et blocage de la création de comptes en doublon.
- **Qualité Logicielle** :
    - Refonte du workflow de gestion des dossiers salariés (`EmployeeRecord`) pour une meilleure gestion des états et des transitions.
    - Optimisation de la suite de tests (exécution parallélisée en 4 segments pour réduire le temps de CI).

### Autres changements
- Mise à jour de la documentation technique concernant le parsing des données entrantes.
- Nettoyage du code (suppression de fichiers statiques, de commandes de gestion et de styles CSS inutilisés).
