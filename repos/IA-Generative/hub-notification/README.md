# Plateforme de notifications intelligentes et multicanales
Composant du socle IA 
(en construction)

## Finalité

La plateforme de notifications intelligentes est un composant transverse du socle d’IA et de services numériques.
Elle permet d’orchestrer, prioriser et diffuser des notifications pertinentes à destination des agents et des usagers, à travers l’ensemble des applications ministérielles, de manière cohérente, sécurisée et maîtrisée.

Ce composant vise à :
	•	réduire la fragmentation des notifications entre applications,
	•	améliorer la qualité de l’information transmise (bon message, bon canal, bon moment),
	•	offrir une expérience utilisateur unifiée, centrée sur l’action et non sur la surcharge informationnelle.

⸻

## Positionnement dans le socle IA

La plateforme s’inscrit comme un service commun au même titre que :
	•	l’agent conversationnel,
	•	les services de résumé et de transcription,
	•	l’OCR et l’extraction d’entités nommées,
	•	les briques d’automatisation de processus.

Elle constitue le backbone événementiel et attentionnel du SI, capable de transformer des événements techniques ou métier en notifications intelligibles et actionnables, y compris enrichies par des capacités IA (priorisation, regroupement, contextualisation).

⸻

## Principes structurants

1. Architecture événementielle

Les applications métiers ne “poussent” pas directement des messages aux utilisateurs.
Elles émettent des événements métier normalisés (ex. : Dossier déposé, Action attendue, Incident ouvert), qui sont ensuite interprétés et orchestrés par la plateforme.

👉 Découplage fort entre production d’événements et diffusion des notifications.

⸻

### 2. Orchestration centralisée des notifications

Un service cœur :
	•	applique les règles de diffusion,
	•	respecte les préférences utilisateurs et organisationnelles,
	•	sélectionne les canaux appropriés (in-app, email, Teams, push…),
	•	garantit la traçabilité et la résilience.

👉 Une logique unique, cohérente et gouvernable à l’échelle ministérielle.

⸻

### 3. Expérience utilisateur unifiée

Chaque utilisateur dispose d’une boîte de réception in-app transverse, intégrée aux applications :
	•	compteur de notifications,
	•	états (lu, non lu, archivé),
	•	liens directs vers les objets métier concernés,
	•	historique et traçabilité.

👉 Fin de la dispersion entre emails, messages Teams et alertes applicatives isolées.

⸻

### 4. Gouvernance, sécurité et conformité

Le composant applique des principes stricts de :
	•	minimisation des données (références plutôt que contenus sensibles),
	•	traçabilité complète des notifications et des accès,
	•	scoping organisationnel (multi-entités, multi-directions),
	•	gestion des préférences utilisateur et collectives.

⸻

## Capacités fonctionnelles clés

🔔 Notifications multicanales
	•	In-app (temps réel ou différé)
	•	Email (immédiat ou digest)
	•	Push mobile (si autorisé)
	•	Outils collaboratifs (Teams, Slack)
	•	SMS (cas d’usage critiques)

⸻

🧠 Gestion intelligente de la diffusion
	•	Priorisation (faible / normale / élevée)
	•	Fenêtrage temporel (“quiet hours”, jours ouvrés)
	•	Digests (quotidiens / hebdomadaires)
	•	Déduplication et idempotence

⸻

📣 Campaign Manager (fonction avancée)

Une brique d’orchestration permet de :
	•	cibler des populations (rôles, directions, projets),
	•	planifier des campagnes,
	•	gérer des parcours de relance (ex. : J+2 si aucune action),
	•	versionner et localiser les messages,
	•	mesurer l’impact (ouverture, clic, action).

⸻

## Modèle de notification unifié

Chaque notification repose sur un objet canonique, garantissant l’interopérabilité :
	•	identifiant unique et clé d’idempotence,
	•	type d’événement métier,
	•	destinataire (utilisateur ou groupe),
	•	canaux de diffusion,
	•	contenu (titre, message, métadonnées),
	•	lien vers l’objet métier,
	•	statut par canal,
	•	durée de vie et archivage.

⸻
## 💡 👉 Script d’exemple : envoi d’une notification via NATS dans openWebUI 💡

Un script minimal est fourni pour illustrer l’envoi d’une notification dans le bus de messages, sans dépendre d’une application métier.

📄 Fichier : `infrastructure/scripts/post_banner_nats.sh`

Ce script :
	•	construit un message de notification au format JSON,
	•	génère automatiquement un identifiant unique (UUID) pour garantir l’idempotence,
	•	ajoute un horodatage Unix,
	•	publie le message sur un sujet NATS configurable.

Variables utilisées :
	•	`NATS_SUBJECT` : sujet NATS de publication (par défaut `notifications.test`)
	•	Arguments du script :
		1. Titre de la notification
		2. Contenu du message
		3. Type (`info`, `warning`, `error`, `success`)
		4. Message dismissible (`true` / `false`)

Exemple d’utilisation :
```
export NATS_SUBJECT="notifications.test"
./scripts/post_banner_nats.sh \
  "Maintenance programmée" \
  "Une intervention est prévue à 18h" \
  "warning" \
  "false"
```

Le message publié est ensuite :
	•	consommé par le listener `openwebui-banner-listener`,
	•	transformé en bannière applicative,
	•	affiché en temps réel dans l’interface OpenWebUI.

👉 Ce script constitue un **outil de test, de démonstration et de debug**, et préfigure la manière dont des applications métiers publieront leurs événements dans le Hub de notifications.

⸻

## Architecture de référence

La plateforme s’appuie sur :
	•	un bus de messages (Kafka, RabbitMQ, NATS…),
	•	le pattern Outbox pour garantir la cohérence transactionnelle,
	•	un Notification Store centralisé,
	•	des connecteurs pluggables vers les canaux de diffusion,
	•	une observabilité complète (logs, métriques, DLQ).

👉 Architecture robuste, scalable et alignée avec les standards cloud et souverains.

![Schéma d’architecture – Hub Notification](images/schematic-hub.png)

⸻

Déploiement progressif (approche MVP)

Phase 1 – Notifications in-app
	•	événements métier prioritaires,
	•	inbox utilisateur,
	•	règles simples.

Phase 2 – Multicanal et tracking
	•	email, digests,
	•	suivi des statuts,
	•	gestion des erreurs.

Phase 3 – Orchestration avancée
	•	campagnes,
	•	segmentation,
	•	workflows et mesure d’impact.

⸻

Bénéfices clés pour le ministère
	•	✔️ Réduction de la surcharge informationnelle
	•	✔️ Meilleure adoption des services numériques
	•	✔️ Traçabilité et gouvernance renforcées
	•	✔️ Socle réutilisable pour tous les produits
	•	✔️ Pré-requis pour des usages IA avancés (priorisation, résumé, recommandation)

⸻
