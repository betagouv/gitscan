## Changelog : les-emplois (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte de l'identité visuelle de la plateforme (rebranding) et une amélioration significative de l'expérience utilisateur. Les bénéficiaires disposent désormais d'un nouvel onglet "Aperçu" pour centraliser leurs informations clés, et les professionnels bénéficient d'outils de suivi plus précis, notamment via des alertes de fin de contrat et une gestion simplifiée des accompagnements.

### Évolutions fonctionnelles
- **Identité et interface** :
    - Refonte de l'identité visuelle (rebranding) incluant le changement de nom, la mise à jour des logos et l'actualisation des pages légales et d'accessibilité.
    - Refonte de la page d'accueil (landing page).
    - Réorganisation des menus pour les employeurs et les prescripteurs afin de faciliter la navigation.
- **Suivi des bénéficiaires (Job Seekers)** :
    - Création d'un nouvel onglet "Aperçu" centralisant les informations sur les conseillers, les contrats et la dernière candidature.
    - Mise en place de bannières et de compteurs d'alerte pour signaler les fins de contrat imminentes aux employeurs et prescripteurs.
    - Amélioration de la gestion des accompagnements : possibilité de créer, modifier ou archiver des affectations directement depuis l'interface.
- **Gestion des PASS IAE** :
    - Internalisation du processus de clôture des PASS IAE via un formulaire interne (remplaçant l'outil Tally) et ajout de notifications automatiques pour les bénéficiaires.
- **Recherche et Administration** :
    - Amélioration des filtres de recherche pour les villes et les structures.
    - Ajout de fonctionnalités de gestion des liens magiques d'orientation pour l'administration.

### Évolutions techniques
- **Traçabilité et Audit** :
    - Implémentation d'une piste d'audit (audit trail) de base et ajout d'un identifiant de navigateur pour améliorer la précision des logs.
- **Reporting et Données (Metabase)** :
    - Optimisation des tableaux de bord Metabase, incluant la création de nouvelles tables pour le suivi GEIQ et l'amélioration des requêtes de transition.
    - Organisation du schéma de données pour le reporting.
- **API et Sécurité** :
    - Affinement des périmètres de sécurité (scopes) des API.
    - Renforcement de la protection des données personnelles en filtrant les identités des bénéficiaires dans les logs Sentry.
- **Automatisation et Maintenance** :
    - Ajout de commandes de gestion (management commands) pour la détection de fichiers manquants et la récupération de pièces jointes.
    - Optimisation de certaines tâches planifiées (cron jobs) pour améliorer les performances de traitement.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique, notamment sur le SSO et la configuration de l'environnement local.
- **Qualité et UI** : Nettoyage important de la typographie, des espaces et de la formulation des messages d'erreur et d'aide sur l'ensemble de la plateforme.
- **Accessibilité** : Ajout d'une déclaration d'accessibilité détaillant les non-conformités et exemptions.
