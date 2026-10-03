## Changelog : dig-dig-doc (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois a marqué une étape majeure avec le lancement des capacités de génération de documents intelligents et l'amélioration profonde de l'analyse de dossiers. Les utilisateurs peuvent désormais créer des brouillons de documents basés sur des modèles, les prévisualiser en PDF et les exporter en formats ODT ou PDF. L'intelligence artificielle est plus intégrée que jamais, avec un assistant conversationnel directement accessible depuis les dossiers et une nouvelle fonctionnalité "éphémère" permettant des analyses rapides et temporaires.

### Évolutions fonctionnelles

**Génération et gestion de documents**
- Mise en place de modèles de documents versionnés avec définition de champs personnalisés ([#138](https://github.com/IA-Generative/dig-dig-doc/issues/138), [#140](https://github.com/IA-Generative/dig-dig-doc/issues/140)).
- Création de brouillons de documents avec génération automatique des valeurs de champs par agent IA ([#141](https://github.com/IA-Generative/dig-dig-doc/issues/141)).
- Système d'assemblage, de stockage et de téléchargement des documents générés en formats ODT et PDF ([#143](https://github.com/IA-Generative/dig-dig-doc/issues/143)).
- Ajout de la prévisualisation PDF et de la traçabilité des sources pour les brouillons ([#142](https://github.com/IA-Generative/dig-dig-doc/issues/142)).
- Administration des modèles de documents et des prompts de génération via l'interface.

**Analyse de dossiers et intelligence**
- Nouveau modèle de données pour l'analyse de dossier incluant l'historique, la provenance et les propositions ([#112](https://github.com/IA-Generative/dig-dig-doc/issues/112), [#116](https://github.com/IA-Generative/dig-dig-doc/issues/116)).
- Possibilité d'ajouter des notes internes versionnées avec des suggestions de l'IA ([#117](https://github.com/IA-Generative/dig-dig-doc/issues/117)).
- Amélioration de la fiabilité avec des relances incrémentales et la conservation des apports lors des mises à jour d'analyse ([#119](https://github.com/IA-Generative/dig-dig-doc/issues/119)).
- Système de validation des propositions avec journal de modification ([#114](https://github.com/IA-Generative/dig-dig-doc/issues/114)).

**Expérience Chat et Assistant**
- Refonte de l'interface de chat (style ChatGPT) avec affichage des étapes d'exécution des outils et des sources de données ([#104](https://github.com/IA-Generative/dig-dig-doc/issues/104)).
- Accès direct à l'assistant conversationnel depuis le chat d'un dossier.
- Amélioration de la navigation : pagination des messages et des listes de conversations, et gestion du mode responsive.

**Nouveautés et mode Éphémère**
- Introduction du mode "Éphémère" : permet de réaliser des analyses rapides qui sont automatiquement supprimées après exécution ([#22](https://github.com/IA-Generative/dig-dig-doc/issues/22), [#23](https://github.com/IA-Generative/dig-dig-doc/issues/23)).
- Disponibilité de nouveaux SDK Python pour l'utilisation standard et éphémère de la plateforme.
- Ajout d'une page profil utilisateur avec statistiques et accès aux tutoriels.

### Évolutions techniques

**Infrastructure et Backend**
- Déploiement d'un nouveau worker dédié au rendu de documents via LibreOffice ([#146](https://github.com/IA-Generative/dig-dig-doc/issues/146), [#148](https://github.com/IA-Generative/dig-dig-doc/issues/148)).
- Refactorisation des variables de configuration S3 pour respecter les standards AWS.
- Amélioration de l'observabilité avec l'implémentation de logs au format JSON et des healthchecks étendus (Postgres, S3, Celery).
- Optimisation du déploiement via Helm et KEDA (configuration du nombre minimal de réplicas).
- Support du protocole MCP (Model Context Protocol) via un serveur dédié.

**Frontend**
- Intégration du Design System de l'État (DSFR) pour une interface plus cohérente et professionnelle.
- Refactorisation des composants (notamment le sélecteur de modèles) pour une meilleure réutilisation.

**CI/CD et Qualité**
- Automatisation complète du cycle de release (images, charts Helm, versions).
- Renforcement de la pipeline CI avec l'intégration de GitLab CI et de tests de contrat OpenAPI.

### Autres changements

**Documentation**
- Rédaction de la documentation pour l'API éphémère et l'utilisation du serveur MCP.
- Mise à jour des README et des plans de tests de bout en bout.
