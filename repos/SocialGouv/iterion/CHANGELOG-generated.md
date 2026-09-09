## Changelog : iterion (30 derniers jours, au 08/09/2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la résilience et de l'observabilité du plan de contrôle. Les capacités de récupération des agents ont été améliorées (points de contrôle, reprises de sessions), et de nouveaux outils de surveillance ont été introduits, notamment pour la détection de vulnérabilités et l'accessibilité. La gestion des budgets et des ressources est devenue plus fine, offrant un meilleur contrôle sur l'exécution des flux de travail complexes.

### Évolutions fonctionnelles
- **Nouvelles capacités d'agents et de surveillance :**
    - Introduction de **Senti**, une sentinelle de vulnérabilités basée sur l'inventaire sans recours systématique aux LLM ([#515](https://github.com/SocialGouv/iterion/issues/515)).
    - Ajout d'un auditeur d'accessibilité (**Ultra11y**) pour garantir la conformité des résultats ([#409](https://github.com/SocialGouv/iterion/issues/409)).
    - Exposition de la recherche web native via les outils du DSL ([#550](https://github.com/SocialGouv/iterion/issues/550)).
    - Mise en place de niveaux de revue par dépôt (glance / guard / audit) ([#742](https://github.com/SocialGouv/iterion/issues/742)).
- **Améliorations de l'expérience utilisateur :**
    - Possibilité de forcer un redémarrage complet ("Retry from zero") depuis le tableau de bord ([#954](https://github.com/SocialGouv/iterion/issues/954)).
    - Synchronisation des tableaux GitHub Projects v2 avec le tableau natif d'Iterion ([#745](https://github.com/SocialGouv/iterion/issues/745)).
    - Visibilité accrue sur les capacités des modèles (prix et limites de sortie) ([#575](https://github.com/SocialGouv/iterion/issues/575)).
    - Aperçu du contenu (JSON, Markdown, texte) directement sur les interfaces de validation humaine dans le Studio ([#425](https://github.com/SocialGouv/iterion/issues/425)).
- **Gestion des ressources :**
    - Possibilité de définir des limites de consommation (usage caps) basées sur un pourcentage de la limite du fournisseur ([#438](https://github.com/SocialGouv/iterion/issues/438)).

### Évolutions techniques
- **Résilience et exécution (Runtime & Sandbox) :**
    - Amélioration de la récupération des points de contrôle (checkpoints) des espaces de travail pour les exécutions interrompues ([#988](https://github.com/SocialGouv/iterion/issues/988)).
    - Optimisation de la gestion des processus : annulation complète des groupes de processus et meilleure gestion des reprises de session ([#935](https://github.com/SocialGouv/iterion/issues/935), [#470](https://github.com/SocialGouv/iterion/issues/470)).
    - Amélioration de l'isolation sur Kubernetes : gestion des demandes de ressources et répartition des nœuds (soft node spread) pour les pods d'exécution ([#694](https://github.com/SocialGouv/iterion/issues/694)).
    - Correction des fuites de processus et de la gestion des répertoires de travail lors des exécutions en sandbox ([#822](https://github.com/SocialGouv/iterion/issues/822), [#766](https://github.com/SocialGouv/iterion/issues/766)).
- **Sécurité et Identité :**
    - Support des jetons de configuration Claude bruts et empreinte numérique des jetons ([#948](https://github.com/SocialGouv/iterion/issues/948)).
    - Migration des identifiants LLM de la plateforme vers une gestion basée sur la base de données pour permettre la rotation sans redéploiement ([#466](https://github.com/SocialGouv/iterion/issues/466)).
    - Renforcement de l'autorisation des écritures liées aux équipes pour éviter les erreurs de tenant ([#997](https://github.com/SocialGouv/iterion/issues/997)).
- **Observabilité et Infrastructure :**
    - Intégration de **Sentry/GlitchTip** pour le suivi des erreurs et la standardisation des logs ([#459](https://github.com/SocialGouv/iterion/issues/459)).
    - Mise en place de la réplication des flux JetStream pour assurer la haute disponibilité des données ([#592](https://github.com/SocialGouv/iterion/issues/592)).
    - Accélération de la CI en exécutant la suite de tests E2E en parallèle ([#880](https://github.com/SocialGouv/iterion/issues/880)).

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique, incluant les bilans d'exploitation (dogfooding), les procédures de déploiement Cloud et les guides sur les limites de consommation ([#756](https://github.com/SocialGouv/iterion/issues/756), [#832](https://github.com/SocialGouv/iterion/issues/832), [#403](https://github.com/SocialGouv/iterion/issues/403)).
- **Tests :** Amélioration des frameworks de test *Golden Master* et *Modernize* pour une meilleure détection des dérives de code ([#882](https://github.com/SocialGouv/iterion/issues/882), [#750](https://github.com/SocialGouv/iterion/issues/750)).
