## Changelog : template-proto (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'automatisation du déploiement et de la configuration initiale du prototype. L'intégration de Coolify a été grandement améliorée, permettant une provision automatique et une meilleure gestion des secrets. Des corrections et optimisations ont également été apportées pour assurer la compatibilité avec les dernières versions du Design System Fr et améliorer la stabilité générale.

### Évolutions fonctionnelles
- **Provisionnement automatique de Coolify :** Le prototype provisionne maintenant automatiquement une instance Coolify lors du premier déploiement, simplifiant grandement la mise en route. Le statut de cette provision est rapporté dans l'interface `/save`.
- **Compatibilité DSFR v1.32 :** Le prototype est maintenant compatible avec la version 1.32 du Design System Fr, incluant les changements d'API liés à l'App Router.
- **Personnalisation du README :** Un README orienté PM est maintenant généré automatiquement, avec une personnalisation basée sur les informations du projet.

### Évolutions techniques
- **Amélioration de l'agent VM :**
    - La taille de la VM de l'agent a été ajustée à plusieurs reprises pour optimiser les performances (8GB/30GB/4 cpus, puis 16GiB/40GiB/6 cpus, et finalement retour aux valeurs par défaut).
    - Suppression des installations npm globales inutiles dans la VM de l'agent.
    - Refactorisation du script de runtime de la VM de l'agent (scripts/runtime.sh renommé en .agent-vm.runtime.sh).
    - Utilisation de flags CLI pour passer les ressources à la VM de l'agent au lieu d'un fichier de configuration.
- **Gestion des migrations Drizzle :** Le prototype ignore maintenant les migrations Drizzle si aucun journal Drizzle n'existe.
- **Sécurité :** Renommage du secret `COOLIFY_TOKEN` en `COOLIFY_TOKEN_WRITE` pour plus de clarté.
- **Assets DSFR :** Les assets statiques du Design System Fr sont maintenant servis depuis le dossier `public/` au lieu d'être inclus dans le bundle.
- **Reproductibilité des builds :** Ajout du fichier `package-lock.json` pour garantir des builds reproductibles.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés au script de runtime de la VM de l'agent.
- Correction de la capture de l'URL de la base de données interne depuis la réponse de création de Coolify.
- Scaffold initial du projet.
