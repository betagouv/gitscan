## Changelog : les-emplois (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure avec son rebranding sous le nom de "La plateforme de l'inclusion", incluant une mise à jour complète de l'identité visuelle. Les utilisateurs bénéficieront d'une gestion des orientations beaucoup plus fluide et automatisée, ainsi que d'un nouvel espace de suivi pour les candidats. Côté technique, le système est devenu plus robuste et traçable grâce à l'implémentation d'un journal d'audit et à une mise à jour majeure de l'environnement Python.

### Évolutions fonctionnelles
- **Identité visuelle et accessibilité** : Rebranding complet vers "La plateforme de l'inclusion" (nouveaux logos, noms et mentions légales) et ajout d'une déclaration d'accessibilité détaillée.
- **Parcours d'orientation (Insertion)** : 
    - Refonte complète de l'interface (wizard d'orientation et pages de détails pour les services et structures).
    - Automatisation des notifications par email (création, acceptation, refus, rappels automatiques aux structures et expiration).
    - Ajout de fonctionnalités de gestion : motifs de refus détaillés, dates de création et expiration automatique des orientations.
- **Expérience Candidat (Usager)** : 
    - Création d'un nouvel onglet "Vue d'ensemble" sur le profil usager regroupant les informations clés (conseillers, fin de contrat, dernières candidatures).
    - Ajout d'un onglet dédié au suivi des orientations.
- **Recherche et Visibilité** : 
    - Amélioration des résultats de recherche de services (affichage des modes de mobilisation et des délais de réponse attendus).
    - Ajout d'une option de visibilité pour les professionnels dans l'Annuaire Pro.
- **Gestion des candidatures** : Fermeture automatique des recrutements en cas de refus pour le motif "pas de recrutement en cours".

### Évolutions techniques
- **Infrastructure et Performance** : 
    - Migration vers Python 3.14.
    - Optimisation du temps de démarrage du service (gain de 600ms).
- **Sécurité et Traçabilité** : 
    - Implémentation d'une piste d'audit (audit trail) pour suivre les actions utilisateurs, les adresses IP et les navigateurs.
    - Renforcement de la gestion de l'authentification (ProConnect et OpenID Connect) avec mise en cache des clés JWKS.
- **Gestion des dossiers employés (Employee Record)** : Refonte majeure du workflow (nouveaux états, gestion des transitions de statut et amélioration de la gestion des erreurs de synchronisation).
- **Système de communication** : Migration des modèles d'emails vers le format Markdown et amélioration de la compatibilité des messages (alternance HTML/Texte).
- **Qualité logicielle** : Amélioration de la robustesse des tests automatisés et optimisation des processus de CI/CD (notamment pour les "review apps").

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant le SSO et la piste d'audit.
- **Maintenance** : Nettoyage du code et suppression de fonctionnalités obsolètes (modules Nexus, dépendances DORA inutilisées).
