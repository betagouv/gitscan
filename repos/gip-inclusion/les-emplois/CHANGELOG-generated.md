## Changelog : les-emplois (30 derniers jours, au 14/10/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'identité visuelle de la plateforme, désormais nommée "La plateforme de l'inclusion", et par une amélioration significative de l'expérience utilisateur. Les fonctionnalités liées à l'insertion ont été profondément modernisées avec un nouveau tunnel d'orientation automatisé et un système de notifications par email. La visibilité des parcours usagers a également été renforcée grâce à de nouveaux outils de pilotage et des vues de profil enrichies.

### Évolutions fonctionnelles
- **Identité et Interface** : 
    - Renommage global de la plateforme en "La plateforme de l'inclusion" (logos, textes légaux, documentation).
    - Harmonisation de l'iconographie des organisations et amélioration de la mise en page des formulaires.
    - Changement de terminologie : utilisation privilégiée du terme "usager" au lieu de "candidat".
- **Parcours Usager** : 
    - Création d'un nouvel onglet "Aperçu" sur le profil de l'usager, centralisant les informations sur les contrats, les conseillers et les dernières candidatures.
    - Ajout d'un badge visuel pour identifier les usagers résidant en zone QPV (Quartier Prioritaire de la Politique de la Ville).
- **Gestion de l'Insertion** : 
    - Refonte complète du tunnel d'orientation (redesign des pages de détail et de structure).
    - Automatisation du cycle de vie des orientations : expiration automatique, gestion des motifs de refus et envoi de notifications par email (acceptation, refus, rappels).
    - Possibilité pour les prestataires de services d'accepter ou de décliner une orientation directement via l'interface.
- **Recherche et Pilotage** : 
    - Amélioration de la recherche de services avec l'affichage des modes de mobilisation et des délais de réponse attendus.
    - Mise en place de nouveaux tableaux de bord de pilotage (export Metabase, indicateurs GEIQ, suivi des fins de parcours).
- **Candidatures** : 
    - Fermeture automatique des recrutements en cas de refus motivé par une absence de poste disponible.

### Évolutions techniques
- **Infrastructure et Environnement** : 
    - Migration de l'environnement vers Python 3.14.
    - Optimisation des processus de déploiement et de la CI.
- **Sécurité et Authentification** : 
    - Renforcement de l'authentification via ProConnect (gestion des clés JWKS, audit trail amélioré).
    - Amélioration de la traçabilité des actions (audit trail) incluant la capture des adresses IP et des informations de navigation.
    - Sécurisation de la création de comptes pour éviter les doublons.
- **Gestion des données et Workflow** : 
    - Refonte du système de gestion des dossiers employés (*Employee Records*) avec un nouveau workflow de statuts et une gestion plus robuste des fichiers joints.
    - Optimisation des performances de l'interface d'administration, notamment sur les tables volumineuses (pagination et hiérarchie des dates optimisées).
- **Qualité logicielle** : 
    - Nettoyage important du code (suppression de modules et de pages obsolètes comme "nexus").
    - Amélioration de la robustesse des tests et de la gestion des erreurs de type.

### Autres changements
- Mise à jour de la documentation technique et des commentaires de code.
- Amélioration de la qualité du code via le renforcement des règles de linting (Ruff, DjLint).
- Amélioration de la gestion des emails (support du format Markdown et amélioration des signatures).
