## Changelog : territoires-en-transitions (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par une intégration majeure de l'intelligence artificielle pour automatiser l'importation et la classification des plans de transition. La plateforme a également évolué pour offrir une gestion plus fine des leviers d'action des collectivités et a préparé la transition vers le nouveau référentiel CR, tout en renforçant la robustesse de la gestion documentaire.

### Évolutions fonctionnelles
- **Intelligence Artificielle (Bêta) :** 
  - Introduction d'un outil d'importation de plans assisté par l'IA (Gemini), permettant la classification automatique des fiches par levier.
  - Mise en place d'un contrôle humain obligatoire : les plans importés par IA doivent être vérifiés avant le dépôt du PCAET.
  - Système de quotas pour limiter l'utilisation des ressources IA par collectivité.
- **Gestion des Collectivités & Leviers :**
  - Refonte de l'interface des leviers : affichage détaillé des catégories, des actions rattachées et de la mobilisation par volet.
  - Ajout d'un système de notation (0 à 3) pour évaluer la mobilisation d'une collectivité sur chaque volet.
  - Gestion des périmètres géographiques secondaires pour les EPCI.
- **Suivi des PCAET & Instructions :**
  - Amélioration du cycle d'instruction avec un vocabulaire de statuts unifié et des notifications automatiques pour les services et pilotes.
  - Meilleure visibilité sur les dossiers en cours d'élaboration et les dépôts effectués hors plateforme.
- **Référentiels & Indicateurs :**
  - Automatisation du calcul des scores indicatifs en fonction des valeurs d'indicateurs et de leur suivi.
  - Possibilité pour les utilisateurs de déclarer un indicateur comme "non applicable".
  - Déploiement de la procédure de bascule vers le référentiel CR (avec modale de confirmation et gestion des archives).
- **Gestion Documentaire :**
  - Possibilité de télécharger l'ensemble des documents d'une mesure via une archive ZIP.
  - Amélioration de la gestion des fichiers volumineux et des doublons lors du dépôt.

### Évolutions techniques
- **IA & LLM :** Migration de l'appel aux modèles vers Vertex AI (Gemini) via un compte de service backend pour une meilleure gestion de la sécurité et des quotas.
- **Architecture & Refactoring :**
  - Suppression définitive du module "Panier" et de ses composants associés.
  - Migration de la gestion des formulaires de contact vers un endpoint backend dédié.
  - Refonte du système de dépôt de documents utilisant des jetons signés et le transport résumable.
- **Infrastructure & CI/CD :**
  - Mise en place de Nx Cloud pour optimiser les performances des builds et des tests.
  - Transition des processus de déploiement vers des Dockerfiles natifs (sortie d'Earthly).
  - Optimisation des workflows de maintenance de la base de données et de la CI.
- **Outils de support :** Enrichissement de l'intégration avec Crisp pour permettre aux agents de support de visualiser les informations CRM directement dans les conversations.

### Autres changements
- **Documentation :** Mise à jour importante des décisions d'architecture (ADR) concernant la périodicité des indicateurs, l'utilisation de l'IA et les stratégies de déploiement.
- **Nettoyage :** Suppression de nombreuses fonctions obsolètes (Supabase edge functions, vues inutilisées) et de code mort.
