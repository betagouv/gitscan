#!/usr/bin/env python3
"""
Analyse labels.csv and group labels into semantic categories per type.
Uses all items; outputs at most 50 relevant categories per type (~150 total).

Output: analyze_labels_output.md  +  analyze_labels_output.json
"""

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Normalisation & matching
# ---------------------------------------------------------------------------

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def matches(label: str, keywords: list[str]) -> bool:
    """
    Keyword prefixes:
      =word   exact whole-label match  (label == word)
      ^word   label starts with word
      default substring match
    """
    for kw in keywords:
        if kw.startswith("="):
            if label == kw[1:]:
                return True
        elif kw.startswith("^"):
            if label.startswith(kw[1:]):
                return True
        else:
            if kw in label:
                return True
    return False


# ---------------------------------------------------------------------------
# Category rules — ordered, first match wins.
# ---------------------------------------------------------------------------

RULES: dict[str, list[tuple[str, list[str]]]] = {

    # ── FEATURES (35 categories) ────────────────────────────────────────────
    "features": [
        # Put AI early to catch "génération / recommandations / chatbot" before
        # they fall into document or data categories.
        ("Intelligence Artificielle & NLP",
         ["traitement du langage", "reconnaissance optique",
          "reconnaissance d'entités", "transcription",
          "recommandations personnalisées", "chatbot",
          "génération de quiz", "génération de secrets",
          "génération de pdf", "génération de documents",
          "modèle de langage", "modèles de langage", "nlp",
          "intelligence artificielle", "apprentissage automatique",
          "clustering", "classification automatique", "ocr"]),

        ("Authentification & Accès",
         ["authentif", "login", "connexion", "oidc", "oauth", "saml",
          "2fa", "mfa", "contrôle d'accès", "gestion des accès",
          "réinitialisation du mot de passe"]),

        ("Gestion des utilisateurs & Permissions",
         ["gestion des utilisateurs", "gestion des droits",
          "gestion des rôles", "permissions", "gestion des contacts",
          "annuaire", "rôles des membres", "gestion des comptes",
          "gestion des groupes", "gestion des membres",
          "organisations", "groupes"]),

        ("Gestion des équipes & Partenaires",
         ["gestion des équipes", "gestion des organisations",
          "gestion des sponsors", "gestion des partenaires",
          "gestion des applications", "gestion des abonnements",
          "partenaires"]),

        ("Recherche & Filtres",
         ["recherche", "search", "autocomplete", "filtrage", "filtre",
          "préremplissage"]),

        ("Visualisation de données & Cartographie",
         ["visualisation", "cartograph", "géolocalisation", "géocodage",
          "carte ", "map ", "graphique", "dataviz", "chart",
          "affichage de résultats", "affichage des résultats",
          "affichage environnemental", "exploration de données",
          "exploration interactive"]),

        ("Statistiques & Rapports",
         ["statistique", "rapport", "reporting", "tableau de bord",
          "tableaux de bord", "dashboard", "analytics",
          "analyse des données", "analyse de données",
          "analyse des performances", "indicateur", "kpi",
          "analyse temporelle", "analyse contextuelle",
          "analyse de sites web"]),

        ("Notifications & Alertes",
         ["notif", "alerte", "sms", "envoi d'email", "messagerie", "message"]),

        ("Gestion documentaire & Fichiers",
         ["document", "fichier", "pièce jointe", "téléchargement", "upload",
          "import de données", "export de données",
          "extraction de données", "extraction d'information",
          "chargement de données", "classification de document",
          "gestion des pièces jointes", "exportation de données",
          "export csv", "conversion de données", "comparaison de données",
          "analyse de fichiers", "analyse de documents"]),

        ("Données & Schémas",
         ["transformation de données", "traitement de données",
          "synchronisation de données", "collecte de données",
          "intégration de données", "pipeline", "etl",
          "modélisation de données", "interopérabilité des données",
          "gestion des données", "gestion de données",
          "définition de schéma", "gestion des jeux de données",
          "anonymisation des données", "ingestion",
          "gestion des métadonnées", "affichage des sources"]),

        ("API & Intégrations",
         ["api rest", "api ", "api", "webhook",
          "intégration", "synchronisation"]),

        ("Administration & Backoffice",
         ["interface d'administration", "administration",
          "back-office", "backoffice", "gestion des configurations",
          "configuration", "déploiement continu", "auto-hébergement"]),

        ("Formulaires & Démarches",
         ["formulaire", "questionnaire", "démarche", "inscription",
          "candidature", "dossier", "demande", "gestion des procédures",
          "gestion des habilitations"]),

        ("Simulation & Calcul",
         ["simulat", "calcul", "empreinte carbone",
          "impact environnemental", "estimat", "prévision", "modélisat"]),

        ("Interface utilisateur & Design",
         ["composants d'interface", "composants réutilisables",
          "interface graphique", "responsive",
          "création de pages", "modification de pages",
          "composants html", "composants dsfr", "compatibilité dsfr",
          "interface utilisateur", "interface web",
          "interface utilisateur web", "interface utilisateur réactive",
          "interface utilisateur moderne", "interface en ligne de commande"]),

        ("Tableaux & Affichage",
         ["tableau", "grille", "liste", "kanban", "pagination",
          "affichage d'informations", "widgets personnalisables", "icônes"]),

        ("Collaboration & Workflow",
         ["collaboration", "workflow", "processus",
          "automatisation de tâche", "gestion de projet",
          "gestion des tâches", "gestion des projets",
          "gestion des programmations", "gestion des contributions",
          "partage d'idées", "journaux d'événements"]),

        ("Monitoring & Logs",
         ["surveillance", "monitoring", "logs", "disponibilité",
          "analyse des dépendances", "gestion des logs",
          "gestion des erreurs", "gestion des dépendances",
          "vérification d'url"]),

        ("Sécurité & Conformité",
         ["sécurité", "chiffrement", "conformité", "rgpd", "audit",
          "vulnérabilité", "validation des données", "validation de données",
          "partage sécurisé", "partage de mots de passe",
          "gestion des secrets", "gestion des clés",
          "gestion des certificats", "ingestion sécurisée",
          "envoi sécurisé"]),

        ("Contenu éditorial",
         ["blog", "actualités", "gestion de contenu", "éditeur", "cms",
          "faq", "mentions légales", "politique de confidentialité",
          "contact", "création de sites", "pages d'information",
          "guides", "articles", "conditions générales", "édition markdown"]),

        ("Accessibilité & i18n",
         ["accessibilité", "rgaa", "wcag", "traduction", "i18n",
          "multilingue", "internationalisation",
          "gestion de l'internationalisation"]),

        ("Personnalisation & Thèmes",
         ["personnalisation", "thème", "thèmes personnalisables",
          "gestion des thèmes", "gestion des plugins",
          "personnalisation de l'interface", "personnalisation du style",
          "personnalisation de l'apparence"]),

        ("Suivi & Traçabilité",
         ["suivi des", "suivi de", "traçage", "historique",
          "gestion des versions", "collecte d'événements",
          "suivi des événements", "suivi des progrès"]),

        ("Tests & QA",
         ["tests automatisés", "test d'éligibilité", "validation automatique",
          "qualité du code"]),

        ("Paiement & Facturation",
         ["paiement", "facturation", "facture", "stripe",
          "virement", "prélèvement"]),

        ("Commentaires & Discussions",
         ["commentaire", "discussion", "gestion des conversations",
          "gestion des commentaires", "retour d'expérience", "feedback",
          "avis utilisateur", "collecte de feedback",
          "commentaires personnalisés"]),

        ("Gestion des médias & Assets",
         ["gestion des médias", "gestion des images", "gestion des vidéos",
          "médias", "assets", "icônes de sites", "images et ressources"]),

        ("Aides & Éligibilité",
         ["gestion des aides", "test d'éligibilité", "éligibilité",
          "récupérer la réglementation", "réglementation applicable",
          "politiques"]),

        ("Temps réel & WebSocket",
         ["temps réel", "websocket", "live", "streaming"]),

        ("Gestion des signalements",
         ["signalement", "gestion des signalements",
          "suivi des signalements"]),

        ("Gestion des profils & Comptes",
         ["gestion des profils", "profil utilisateur", "compte utilisateur",
          "gestion des favoris", "gestion des issues",
          "gestion des adresses", "gestion des actions",
          "gestion des arrêtés"]),

        ("Gestion des établissements & Structures",
         ["gestion des établissements", "établissements scolaires",
          "gestion des structures", "gestion des entreprises"]),

        ("Calendrier & Planification",
         ["calendrier", "agenda", "planning", "réservation",
          "gestion des rendez-vous", "planification de rendez-vous",
          "disponibilité"]),

        ("Évaluation & Notation",
         ["évaluation", "notation", "score", "gestion des évaluations"]),

        ("Infrastructure & Stockage",
         ["stockage sur s3", "infrastructure", "déploiement",
          "gestion des applications"]),

        ("Gestion métier générale",
         ["gestion des événements", "gestion d'événements",
          "gestion des inscriptions", "gestion des missions",
          "gestion des dossiers", "gestion des partenaires",
          "gestion des sponsors", "gestion des abonnements",
          "gestion des métadonnées"]),
    ],

    # ── COMPONENTS (40 categories) ──────────────────────────────────────────
    "components": [
        # Specific techs first to avoid being swallowed by broader categories.

        ("Intelligence Artificielle / ML",
         ["modèles de machine learning", "modèles de langage",
          "modèles d'apprentissage", "modèles de langage (llm)",
          "scripts d'entraînement", "scripts d'évaluation",
          "api openai", "api albert", "embeddings",
          "agents mastra", "workflows mastra", "llm", "rag",
          "annotation de données", "données d'entraînement",
          "modèles de données ia"]),

        ("Celery & Queue asynchrone",
         ["celery", "workers celery", "worker celery",
          "tâches asynchrones", "cron jobs", "cron",
          "workers sidekiq", "workers bullmq", "workers asynchrones",
          "workers goodjob", "sidekiq", "bullmq", "delayed job",
          "workers de traitement"]),

        ("Ansible & IaC",
         ["rôles ansible", "playbooks ansible", "ansible",
          "terraform", "infrastructure as code"]),

        ("Publicodes & Règles métier",
         ["modèle publicodes", "règles publicodes", "publicodes",
          "gestion des règles publicodes", "moteur de règles"]),

        ("Templates & Moteurs de rendu",
         ["templates jinja2", "templates ejs", "templates html",
          "templates", "template", "jinja", "ejs",
          "swagger ui", "openapi"]),

        ("Sites statiques & SSG",
         ["site web statique", "génération de site statique",
          "site statique", "générateur de site statique",
          "rapports statiques", "github pages", "mkdocs",
          "jekyll", "gatsby", "hugo", "eleventy"]),

        ("Authentification (composant)",
         ["keycloak pour l'authentification", "keycloak (authentification)",
          "authentification keycloak", "authentification oauth2",
          "authentification oidc", "authentification nextauth",
          "système d'authentification", "thème keycloak",
          "keycloak pour", "authentification passport"]),

        ("Stockage objet",
         ["stockage s3", "stockage d'objets minio", "stockage minio",
          "intégration s3", "minio", "s3 compatible"]),

        ("Reporting & BI",
         ["outil de reporting metabase", "metabase (outil de reporting)",
          "metabase", "rapports statiques", "outil de reporting",
          "visualisations de données", "composants de visualisation"]),

        ("Intégrations services externes",
         ["api grist", "api github", "api matomo", "api client",
          "intégration mattermost", "widgets grist",
          "application github", "api openai", "api brevo",
          "intégration s3", "api hubspot"]),

        ("SIG & Géospatial",
         ["plugin qgis", "cartographie leaflet", "cartographie interactive",
          "qgis", "leaflet", "postgis", "geoserver", "openlayers",
          "tuiles vectorielles", "maplibre"]),

        ("Gestion d'état",
         ["gestionnaire d'état pinia", "gestionnaire d'état redux",
          "gestion de l'état avec zustand", "gestion d'état redux",
          "redux", "pinia", "zustand", "vuex", "mobx",
          "gestionnaire d'état"]),

        ("CMS (Strapi, Wagtail…)",
         ["cms strapi", "cms basé sur wagtail", "strapi",
          "wagtail", "cms wordpress", "contentful",
          "directus", "ghost", "admin directus",
          "administration sonata"]),

        ("ORM & Accès aux données",
         ["orm prisma", "activerecord", "prisma", "sequelize",
          "typeorm", "alembic", "flyway", "drizzle",
          "modèles de données", "schéma de base de données"]),

        ("Webhooks & Événements",
         ["webhooks", "webhook sentry", "webhook dispatcher",
          "webhook d'admission", "webhook", "event bus",
          "pub/sub", "sse"]),

        ("Scripts & Utilitaires",
         ["scripts sql", "scripts de détection", "scripts de préparation",
          "scripts de build", "scripts d'analyse",
          "scripts de migration", "utilitaires",
          "scripts de données", "makefile", "monorepo"]),

        ("Bibliothèques & Packages",
         ["gem ruby", "package r", "pipfile", "bibliothèque ruby",
          "bibliothèque go", "bibliothèque rust",
          "fichiers r markdown", "package python",
          "requirements", "gemfile", "pyproject"]),

        ("Rust & Go",
         ["serveur rust", "bibliothèque rust", "bibliothèque go",
          "backend rust", "backend go", "rust", " go "]),

        ("Pipeline de données",
         ["pipeline de traitement de données", "pipeline etl",
          "pipeline de données", "pipeline ml",
          "scripts de préparation de données", "dbt",
          "airflow", "prefect", "dagster"]),

        ("API REST & GraphQL",
         ["api rest", "api graphql", "api next.js", "api express",
          "api flask", "api fastapi", "api python", "api (", "graphql",
          "api rest (fastapi)", "api rest (express)", "api rest (via axios)",
          "=api"]),

        ("PostgreSQL & SQL",
         ["postgresql", "mysql", "sqlite", "mariadb", "sql server",
          "base de données postgresql", "base de données mysql",
          "base de données sqlite", "base de données (non spécifiée)",
          "base de données"]),

        ("React / Next.js",
         ["frontend react", "frontend next.js", "composants react",
          "react", "next.js", "nextjs"]),

        ("Vue.js / Nuxt",
         ["vue.js", "vue ", "frontend vue", "nuxt", "quasar"]),

        ("Python (scripts & backend)",
         ["scripts python", "backend python", "script python",
          "scripts r", "bibliothèque python", "application python",
          "backend fastapi", "backend flask", "application flask",
          "notebooks jupyter", "notebook jupyter", "package r",
          "fichiers r markdown"]),

        ("Django",
         ["django", "backend django", "application django",
          "frontend wagtail"]),

        ("Node.js / NestJS",
         ["backend node.js", "serveur node.js", "scripts node.js",
          "backend nestjs", "node.js", "nestjs",
          "serveur nodejs", "serveur express", "api express",
          "api rest (express)"]),

        ("Docker & Conteneurs",
         ["docker", "conteneur", "dockerfile", "images docker"]),

        ("CI/CD & Déploiement",
         ["action github", "actions github", "github actions",
          "workflows github actions", "workflows ci/cd",
          "scripts de déploiement", "buildpack", "procfile",
          "fichiers de configuration scalingo", "ci/cd",
          "scripts de compilation", "scripts de configuration",
          "scripts shell", "script shell",
          "github pages", "configuration scalingo",
          "configuration renovate", "workflow de déploiement",
          "workflows de déploiement"]),

        ("MongoDB & NoSQL",
         ["mongodb", "base de données mongodb", "redis", "cache redis",
          "base de données redis", "elasticsearch", "clickhouse"]),

        ("TypeScript / JavaScript",
         ["typescript", "javascript", "frontend typescript",
          "frontend javascript", "bibliothèque typescript",
          "bibliothèque javascript", "backend typescript"]),

        ("Kubernetes & Helm",
         ["kubernetes", "charts helm", "helm"]),

        ("Serveurs web & Proxy",
         ["serveur nginx", "serveur web nginx", "nginx",
          "reverse proxy traefik", "traefik", "serveur web caddy",
          "caddy", "serveur http", "frontend nginx",
          "configuration nginx"]),

        ("HTML / CSS / Templates visuels",
         ["html", "css", "frontend html", "frontend html/css",
          "frontend (html, css, javascript)"]),

        ("Ruby on Rails",
         ["ruby on rails", "backend ruby on rails", "gem ruby"]),

        ("PHP",
         ["backend php", "php"]),

        ("Angular / Svelte / Autres SPA",
         ["angular", "svelte", "frontend angular", "frontend svelte",
          "frontend streamlit", "streamlit", "elm", "ember"]),

        ("Design System (DSFR & UI libs)",
         ["dsfr", "composants dsfr", "composants réutilisables",
          "composants d'interface", "composants mantine",
          "composants bootstrap", "composants gatsby",
          "bibliothèque de composants", "composants web",
          "éléments ui"]),

        ("Documentation & Schémas",
         ["documentation", "documentation markdown", "documentation sphinx",
          "schéma de données", "schéma json", "schémas json",
          "fichiers csv", "configuration yaml",
          "fichiers de configuration yaml", "fichiers de configuration",
          "données json", "exemples de données", "fichiers yaml",
          "fichiers markdown"]),

        ("Tests",
         ["tests unitaires", "tests automatisés", "tests e2e",
          "tests d'intégration", "tests", "test"]),

        ("Microservices & Architecture",
         ["microservices", "interface en ligne de commande",
          "interface utilisateur web", "interface web", "interface",
          "service worker", "cli", "frontend", "backend"]),
    ],

    # ── TAGS (50 categories) ────────────────────────────────────────────────
    # Specific framework/tool categories come BEFORE broad language categories
    # to avoid e.g. "react" being swallowed by "Python" or "r" matching "docker".
    "tags": [
        # ── Frameworks frontend (ordered specific → general) ──────────────
        ("React & Next.js",
         ["react", "nextjs", "next.js", "preact"]),

        ("Vue.js & Nuxt",
         ["vuejs", "vue.js", "nuxt", "=vue", "quasar"]),

        ("Angular, Svelte & autres SPA",
         ["angular", "svelte", "=ember", "=lit"]),

        ("Wagtail, CMS & générateurs statiques",
         ["wagtail", "hugo", "eleventy", "jekyll", "gatsby",
          "bookdown", "docusaurus", "mkdocs", "=cms"]),

        # ── Frameworks backend ────────────────────────────────────────────
        ("Django & FastAPI",
         ["django", "fastapi"]),

        ("Node.js, NestJS & Express",
         ["nodejs", "node.js", "nestjs", "express"]),

        ("Ruby on Rails",
         ["rails", "ruby on rails"]),

        ("Flask, Symfony & autres backend",
         ["flask", "symfony", "laravel", "sinatra", "phoenix"]),

        # ── Langages (after frameworks to avoid mis-categorization) ───────
        ("Python",
         ["python"]),

        ("TypeScript",
         ["typescript"]),

        ("JavaScript",
         ["javascript"]),

        ("Ruby",
         ["ruby"]),

        ("PHP",
         ["php"]),

        ("Java",
         ["java"]),

        ("Go",
         ["=go", "golang"]),

        ("R & Data Science",
         ["=r", "bookdown", "=dash", "shiny", "jupyter"]),

        ("HTML, CSS & Web",
         ["html", "css", "=web", "svg", "sass", "scss",
          "=frontend", "site web"]),

        ("Shell & Scripts",
         ["shell", "=cli", "bash", "=script", "makefile"]),

        ("Autres langages",
         ["elm", "elixir", "scala", "kotlin", "dart", "swift",
          "haskell", "clojure", "rust", "=c#", "=c++"]),

        # ── Bases de données ───────────────────────────────────────────────
        ("Bases de données SQL",
         ["postgresql", "mysql", "sqlite", "mariadb", "postgis",
          "sql server", "oracle"]),

        ("Bases de données NoSQL",
         ["mongodb", "redis", "elasticsearch", "clickhouse",
          "cassandra", "dynamodb", "couchdb"]),

        ("ETL & Pipelines de données",
         ["=etl", "=dbt", "airflow", "prefect", "dagster",
          "=pipeline", "data pipeline", "=jupyter notebook"]),

        # ── Infrastructure & DevOps ────────────────────────────────────────
        ("Docker & Conteneurs",
         ["docker", "=podman", "=containerd"]),

        ("Kubernetes & Helm",
         ["kubernetes", "helm", "=k8s", "=openshift"]),

        ("CI/CD & GitHub Actions",
         ["ci/cd", "github actions", "gitlab ci", "circleci",
          "github", "=gitlab", "travis", "=argocd", "=gitops",
          "=ansible", "github-action"]),

        ("Déploiement & Hosting",
         ["deployment", "déploiement", "scalingo", "ovh", "buildpack",
          "=self-hosting", "=self-hosted", "=heroku", "=vercel",
          "=netlify", "=clever cloud", "=fly.io", "=s3"]),

        ("Monitoring & Observabilité",
         ["monitoring", "matomo", "sentry", "=logs", "grafana",
          "prometheus", "kibana", "datadog", "=opentelemetry",
          "=performance"]),

        ("Sécurité & Auth",
         ["sécurité", "=security", "keycloak", "oauth", "auth",
          "=autorisation", "=rbac"]),

        ("SSO & Identité fédérée",
         ["=sso", "=saml", "openid connect", "=oidc",
          "franceconnect", "proconnect", "=eidas"]),

        ("Git & DevOps",
         ["=git", "=devops", "=backend", "=gitops",
          "=automation", "=automatisation", "=configuration",
          "=backup", "=infrastructure"]),

        ("Tests & Qualité",
         ["=testing", "=tests", "=test", "=audit", "=a11y",
          "=accessibility", "=e2e", "=validation",
          "=quality", "=qa"]),

        ("Accessibilité",
         ["accessibilité", "=accessibilité"]),

        # ── Data & IA ─────────────────────────────────────────────────────
        ("Intelligence Artificielle & LLM",
         ["=ia", "=llm", "=ai", "=rag", "=embeddings", "=gpu",
          "=chatbot", "=bot", "=agent", "=mcp", "=albert",
          "intelligence artificielle", "modèles de langage", "=copilot"]),

        ("NLP & ML",
         ["=nlp", "=ocr", "machine learning", "deep learning",
          "=ml", "=pseudonymisation", "data science", "=streamlit"]),

        ("Données & Open Data",
         ["données", "=data", "open data", "opendata", "open-data",
          "données publiques", "données ouvertes",
          "=csv", "=pdf", "=documents", "=api", "=webhook",
          "=graphql", "=simulation", "=recherche"]),

        ("Standards & Schémas",
         ["=schema", "=schéma", "=yaml", "=json",
          "table schema", "=jsonld", "=xml", "=rdf",
          "=metadata", "=geojson"]),

        ("Reporting & BI",
         ["=statistics", "=visualisation", "=analytics",
          "=dashboard", "=metabase", "=grafana", "=kibana",
          "=superset", "=redash", "=reporting", "=charts",
          "statistiques", "data visualization", "data viz"]),

        ("SIG & Géospatial",
         ["=qgis", "=leaflet", "=sig", "=géocodage", "=postgis",
          "=gtfs", "=netex", "cartographie", "géolocalisation",
          "=openlayers", "=maplibre", "géospatial", "=geojson"]),

        ("Documentation",
         ["=documentation", "=docs", "=readme"]),

        # ── Outils & Misc ────────────────────────────────────────────────
        ("Outils de build & Frontend tooling",
         ["=vite", "=webpack", "=esbuild", "=rollup", "=parcel",
          "=babel", "=turbo", "=yarn", "=pnpm", "=bun"]),

        ("Design System & UI",
         ["design system", "=design-system", "=dsfr", "=ui",
          "=components", "=storybook", "=tailwind", "=bootstrap"]),

        ("Plugins & Extensions",
         ["=plugin", "=theme", "=template", "=widgets", "=extension",
          "=addon"]),

        ("Communication & Messagerie",
         ["=email", "=communication", "=feedback", "=slack",
          "=mattermost", "=teams", "=discord", "=notifications",
          "=collaboration", "=open source", "open source"]),

        ("Self-hosting & Infrastructure réseau",
         ["=self-hosting", "=self-hosted", "=dns", "=nginx",
          "=traefik", "=caddy", "=reverse-proxy", "=proxy"]),

        # ── Écosystème public ─────────────────────────────────────────────
        ("Écosystème beta.gouv / État",
         ["=france", "gouvernement", "=etalab", "administration",
          "proconnect", "franceconnect", "=dsfr", "=anssi",
          "=publicodes", "=grist", "=trackdechets", "data.gouv.fr",
          "=betagouv", "beta.gouv", "=ademe",
          "administration publique"]),

        ("Territoire & Collectivités",
         ["collectivités", "=gouv", "=insee", "=dila",
          "=commune", "=mairie", "=préfecture", "=région",
          "=département"]),

        ("Subventions & Finances publiques",
         ["=subventions", "=aide", "=aides", "finances publiques",
          "=budget", "=devis", "=accompagnement"]),

        ("Legal & Conformité",
         ["=legal", "=nis2", "=rgpd", "=conformité",
          "=droit", "=juridique"]),

        ("Signalement & Inspection",
         ["=signalement", "=inspection", "=vigieau"]),

        # ── Domaines métier ───────────────────────────────────────────────
        ("Santé & Épidémiologie",
         ["=santé", "=covid-19", "=covid", "=épidémie",
          "=vaccination", "=médical", "=hôpital"]),

        ("Transport & Mobilité",
         ["=transport", "=mobilité", "=gtfs", "=mobility",
          "=netex", "=covoiturage", "=vélo"]),

        ("Environnement & Énergie",
         ["=environnement", "=climat", "=déchets", "=pollution",
          "=émissions", "=énergie", "=energie",
          "=biodiversité", "carbone", "développement durable",
          "transition écologique", "=écologie"]),

        ("Eau & Ressources naturelles",
         ["=eau", "gestion de l'eau", "=vigieau",
          "=irrigation", "=inondation"]),

        ("Agriculture & Alimentation",
         ["=agriculture", "=alimentation", "=agri",
          "=élevage", "=agroalimentaire"]),

        ("Éducation & Formation",
         ["=éducation", "=formation", "=école", "=stage",
          "=education", "=apprentissage", "=université"]),

        ("Justice & Droit",
         ["=justice", "=police", "=gendarmerie"]),

        ("Emploi, Social & Logement",
         ["=emploi", "=social", "=insertion", "=logement",
          "=handicap", "=pauvreté"]),
    ],
}

# ---------------------------------------------------------------------------
# Load CSV
# ---------------------------------------------------------------------------

csv_path = Path(__file__).parent / "labels.csv"

rows_by_type: dict[str, list[tuple[str, int]]] = defaultdict(list)

with open(csv_path, newline="", encoding="utf-8") as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        label = normalize(row["label"])
        row_type = row["type"].strip()
        try:
            count = int(row["count"])
        except ValueError:
            count = 1
        if row_type in ("features", "components", "tags"):
            rows_by_type[row_type].append((label, count))

all_items: dict[str, list[tuple[str, int]]] = {
    rtype: sorted(items, key=lambda x: x[1], reverse=True)
    for rtype, items in rows_by_type.items()
}

# ---------------------------------------------------------------------------
# Categorise
# ---------------------------------------------------------------------------

def categorise(label: str, rtype: str) -> str:
    for category, keywords in RULES.get(rtype, []):
        if matches(label, keywords):
            return category
    return "Autre"


def build_categories(items: list[tuple[str, int]], rtype: str):
    cats: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for label, count in items:
        cat = categorise(label, rtype)
        cats[cat].append((label, count))
    return cats

# ---------------------------------------------------------------------------
# Render markdown + JSON
# ---------------------------------------------------------------------------

DESCRIPTIONS = {
    "features":   "Fonctionnalités d'une application web ou logiciel",
    "components": "Composants techniques (frameworks, langages, infra…)",
    "tags":       "Tags simples pour catégoriser l'application",
}

TOP_N = 50

lines: list[str] = ["# Analyse des labels — Top 50 catégories par type\n"]
json_data: dict = {}

for rtype in ("features", "components", "tags"):
    items = all_items.get(rtype, [])
    cats = build_categories(items, rtype)

    sorted_cats = [
        (cat, entries)
        for cat, entries in sorted(
            cats.items(), key=lambda kv: sum(c for _, c in kv[1]), reverse=True
        )
        if cat != "Autre"
    ][:TOP_N]

    lines.append(f"---\n## {rtype.capitalize()} — {DESCRIPTIONS[rtype]}\n")
    lines.append(f"*{len(items)} labels analysés, {len(sorted_cats)} catégories.*\n")

    for cat, entries in sorted_cats:
        total = sum(c for _, c in entries)
        label_list = ", ".join(
            f"{lbl} ({cnt})"
            for lbl, cnt in sorted(entries, key=lambda x: x[1], reverse=True)
        )
        lines.append(f"### {cat}  `total={total}`")
        lines.append(f"{label_list}\n")

    json_data[rtype] = [
        {
            "category": cat,
            "total": sum(c for _, c in entries),
            "labels": [
                {"label": lbl, "count": cnt}
                for lbl, cnt in sorted(entries, key=lambda x: x[1], reverse=True)
            ],
        }
        for cat, entries in sorted_cats
    ]

output_md = Path(__file__).parent / "analyze_labels_output.md"
output_md.write_text("\n".join(lines), encoding="utf-8")
print(f"Done. Output written to {output_md}")

output_json = Path(__file__).parent / "analyze_labels_output.json"
output_json.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Done. Output written to {output_json}")

# ── Summary ──
total_cats = 0
for rtype in ("features", "components", "tags"):
    items = all_items.get(rtype, [])
    cats = build_categories(items, rtype)
    autre = cats.get("Autre", [])
    autre_total = sum(c for _, c in autre)
    named = {k: v for k, v in cats.items() if k != "Autre"}
    total_cats += len(named)
    print(f"\n[{rtype}] {len(items)} labels → {len(named)} named categories "
          f"(Autre: {len(autre)} labels / {autre_total} occurrences)")
    for cat, entries in sorted(named.items(), key=lambda kv: sum(c for _, c in kv[1]), reverse=True):
        total = sum(c for _, c in entries)
        print(f"  {total:5d}  {cat}  ({len(entries)} labels)")
print(f"\nTotal named categories: {total_cats}")
